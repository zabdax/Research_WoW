#!/usr/bin/env python3
"""Static forensic inventory of the Simon-Ellingsen-supplied MPSLPP software.

MASTER DIRECTIVE 2026-08-29 sections 11, 12, 28.

Reads ONLY the frozen copies under research/sources/ellingsen_hobart/
(software/ + documentation/); never modifies any file. Produces:

  research/sources/ellingsen_hobart/analysis/fortran_dependency_map.json
  research/data/ellingsen_fortran_inventory.yaml

Static analysis only: regex-based structural extraction (program units,
INCLUDEs, CALL targets, I/O statements, constants, keyword scans). No
execution, no reconstruction of missing routines (directive section 12).

Usage:  python scripts/ellingsen_fortran_inventory.py
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "research" / "sources" / "ellingsen_hobart"
FORTRAN = SRC / "software" / "mpslpp.f"
MANUAL = SRC / "documentation" / "mpslpp.tex"
OUT_JSON = SRC / "analysis" / "fortran_dependency_map.json"
OUT_YAML = REPO / "research" / "data" / "ellingsen_fortran_inventory.yaml"

PINNED_SHA256 = {
    "software/mpslpp.f": "3274fe719b465825dc9258c60059ffbf2e09102a1ee1f48813f4862484d2080a",
    "documentation/mpslpp.tex": "09cd1e0217088800a369e4ae5038b9008cddd6bd9a4a21f32492d88fc1660d9c",
}

# Library families recognised from call-name prefixes (directive section 12).
LIBRARY_FAMILIES = {
    "CFITSIO": re.compile(r"^FT[A-Z]|^FITSERR$", re.IGNORECASE),
    "SLALIB": re.compile(r"^SLA_[A-Z]", re.IGNORECASE),
    "PGPLOT": re.compile(r"^PG[A-Z]", re.IGNORECASE),
    "McConnell menu software": re.compile(
        r"^(MENU|OPENREAD|OPENWRITE|USER_WAIT|LIB\$\w+|CLEAR_STRING|LOWCASE|UPCASE|NUMBER|THE)$",
        re.IGNORECASE,
    ),
}

UNIT_RE = re.compile(r"^\s*(program|subroutine|function|block\s+data)\s+([A-Za-z_][\w$]*)", re.IGNORECASE)
CALL_RE = re.compile(r"\bcall\s+([A-Za-z_][\w$]*)", re.IGNORECASE)
INCLUDE_RE = re.compile(r"^\s*include\s+'([^']+)'", re.IGNORECASE)
OPEN_RE = re.compile(r"^\s*open\s*\(", re.IGNORECASE)
INQUIRE_RE = re.compile(r"^\s*inquire\s*\(", re.IGNORECASE)
PARAM_RE = re.compile(r"([A-Za-z_][\w$]*)\s*=\s*([+\-]?[\w.]+(?:[eE][+\-]?\d+)?)")
COMMON_RE = re.compile(r"^\s*common\s*/", re.IGNORECASE)
EXTERNAL_RE = re.compile(r"^\s*external\s+(.+?)\s*$", re.IGNORECASE)

KEYWORD_SCANS = [
    "vanvleck", "van vleck", "one-bit", "one bit", "hanning", "fourier",
    "autocorrel", "lag", "quotient", "baseline", "history", "bandwidth",
    "system temperature", "tsys", "calibrat",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_frozen_hashes() -> dict:
    results = {}
    for rel, pinned in PINNED_SHA256.items():
        path = SRC / rel
        if not path.exists():
            results[rel] = {"status": "MISSING", "pinned_sha256": pinned}
            continue
        actual = sha256(path)
        results[rel] = {
            "status": "HASH_VERIFIED" if actual == pinned else "HASH_MISMATCH",
            "pinned_sha256": pinned,
            "actual_sha256": actual,
            "bytes": path.stat().st_size,
        }
    return results


def parse_fortran(text: str) -> dict:
    lines = text.splitlines()
    units, includes, opens, inquires, commons, externals = [], [], [], [], [], []
    call_sites: dict[str, list[int]] = {}
    param_block: list[str] = []
    in_param = False

    for i, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        m = UNIT_RE.match(raw)
        if m:
            units.append({"line": i, "kind": m.group(1).lower(), "name": m.group(2).lower()})
        for inc in INCLUDE_RE.finditer(raw):
            includes.append({"line": i, "file": inc.group(1)})
        if OPEN_RE.match(raw):
            opens.append({"line": i, "text": stripped})
        if INQUIRE_RE.match(raw):
            inquires.append({"line": i, "text": stripped})
        if COMMON_RE.match(raw):
            commons.append({"line": i, "text": stripped})
        em = EXTERNAL_RE.match(raw)
        if em:
            for name in re.split(r"[,\s]+", em.group(1)):
                if name:
                    externals.append({"line": i, "name": name.lower()})
        for cm in CALL_RE.finditer(raw):
            call_sites.setdefault(cm.group(1).lower(), []).append(i)
        if re.match(r"^\s*(parameter|\w+\*?\d*)\s*.*\(.*=.*", raw, re.IGNORECASE) and "parameter" in raw.lower():
            in_param = True
        if in_param:
            param_block.extend(PARAM_RE.findall(raw))
            if stripped.endswith(")"):
                in_param = False

    local_units = {u["name"] for u in units}
    keyword_hits = {
        kw: [ln for ln, raw in enumerate(lines, start=1) if kw in raw.lower()]
        for kw in KEYWORD_SCANS
    }

    dependencies = {}
    for name, sites in sorted(call_sites.items()):
        if name in local_units:
            cls, family = "FOUND", "local (mpslpp.f)"
        else:
            cls = "REFERENCED_BUT_MISSING"
            family = next(
                (fam for fam, rx in LIBRARY_FAMILIES.items() if rx.match(name)),
                "unidentified external library (not supplied)",
            )
        dependencies[name] = {"classification": cls, "library_family": family, "call_lines": sites}
    for ext in externals:
        name = ext["name"]
        if name not in dependencies:
            dependencies[name] = {
                "classification": "REFERENCED_BUT_MISSING",
                "library_family": "declared EXTERNAL in mpslpp.f; body not supplied",
                "call_lines": [],
                "declared_external_line": ext["line"],
            }
    for inc in includes:
        dependencies.setdefault(f"include:{inc['file']}", {
            "classification": "REFERENCED_BUT_MISSING",
            "library_family": "Fortran INCLUDE file referenced but not supplied",
            "call_lines": [],
            "referenced_line": inc["line"],
        })

    wanted = {"cmax", "maxspc", "maxlag", "maxifs", "maxcmp", "maxplt", "maxord",
              "maxhis", "maxpks", "maxgau", "maxday", "maxsrc", "maxpdb",
              "h_tfields", "i_tfields", "c", "pi", "version", "ntsys"}
    return {
        "total_lines": len(lines),
        "program_units": units,
        "includes": includes,
        "common_blocks": commons,
        "open_statements": opens,
        "inquire_statements": inquires,
        "external_declarations": externals,
        "parameters_extracted": {k: v for k, v in param_block if k.lower() in wanted},
        "keyword_scan": {kw: {"count": len(h), "lines_sample": h[:12]} for kw, h in keyword_hits.items()},
        "dependencies": dependencies,
        "dependency_counts": {
            c: sum(1 for d in dependencies.values() if d["classification"] == c)
            for c in ("FOUND", "FOUND_PARTIAL", "REFERENCED_BUT_MISSING", "NOT_REFERENCED", "UNKNOWN")
        },
    }


def parse_manual(text: str) -> dict:
    commands = re.findall(r"\\subsection\*\{([A-Z]+)\}", text)
    return {
        "title": "MPSLPP User Manual version 1.0",
        "author_line": "Simon Ellingsen",
        "documentclass": "article (\\documentstyle, LaTeX 2.09 era)",
        "commands_documented": commands,
        "n_commands_documented": len(commands),
        "key_statements": {
            "data_form_in_correlator_files": "autocorrelation functions",
            "load_pipeline": "FFT + Van Vleck correction (one-bit sampling) during load; optional Hanning smoothing before FFT",
            "quotient": "signal/reference quotient with optional Tsys adjustment (None/Signal/Baseline)",
            "slots": "20 in manual v1.0; source v1.8 raised maxspc to 40",
            "external_ui": "Dave McConnell's menu software",
            "platforms": "VMS (physvax), PC (Lahey Fortran + Phar Lap 386); SunOS port considered",
        },
    }


def main() -> None:
    hash_status = verify_frozen_hashes()
    bad = [k for k, v in hash_status.items() if v["status"] != "HASH_VERIFIED"]
    if bad:
        raise SystemExit(f"FROZEN SOURCE HASH FAILURE: {bad} -- refusing to analyse. Re-freeze from donor originals.")

    fortran = parse_fortran(FORTRAN.read_text(errors="replace"))
    manual = parse_manual(MANUAL.read_text(errors="replace"))

    pipeline = {
        "load_path_per_source_lines": {
            "1_readfit": "call readfit(...) line 603 (external, CFITSIO-based)",
            "2_vanvleck": "call vanvleck(data,nlags) line 797 (external kernel)",
            "3_optional_hanning": "call hanning(...) line 799, gated by smoothing parameter (external kernel)",
            "4_dofft": "call dofft(data,nlags) line 808 (external kernel)",
            "5_quotient": "inline slot arithmetic + adjust_tsys None/Signal/Baseline logic",
            "6_writefit": "call writefit(...) line 1014 (external, adds history extension)",
        },
        "reproducibility_status_per_arrow": {
            "correlator_output_to_fit": "REPRODUCIBLE (files in frozen archive)",
            "fit_to_acf_read": "DEPENDENCY_MISSING (readfit not supplied)",
            "acf_to_spectrum": "DEPENDENCY_MISSING (vanvleck/dofft/hanning not supplied; conventions DOCUMENTED_ONLY)",
            "quotient_calibration": "DOCUMENTED_ONLY (manual QUOTIENT section; executed reference/Tsys choices unknown)",
            "search_analysis_product": "UNKNOWN (no search/analysis layer survives; attributed to Bob Gray per donor)",
        },
    }

    inventory = {
        "inventory_version": "1.0",
        "created_utc": "2026-08-29",
        "directive": "MASTER DIRECTIVE 2026-08-29 sections 11/12/28 (static analysis only)",
        "donor": "Simon Ellingsen (supplied via project owner; original email not locally archived)",
        "donor_supplied_location": "reresearchdatarequestarchivalhobartfollowupobserv/ (workspace root; folder name as received)",
        "hash_verification": hash_status,
        "fortran": {
            "file": "research/sources/ellingsen_hobart/software/mpslpp.f",
            "program_name": "MPSLPP",
            "full_name": "Mt Pleasant Spectral Line Processing Package",
            "author": "S P Ellingsen",
            "version": "1.8",
            "release_date": "19-Jul-1995",
            "rcs_id": "$Id: mpslpp.f,v 1.8 1995/03/24 10:33:51 sellings Exp sellings $",
            "platforms": ["VMS", "PC (Lahey Fortran + Phar Lap 386)"],
            **fortran,
        },
        "documentation": {"file": "research/sources/ellingsen_hobart/documentation/mpslpp.tex", **manual},
        "historical_pipeline": pipeline,
        "prohibitions_respected": {
            "no_missing_routine_reconstructed": True,
            "no_search_rule_inferred": True,
            "no_calibration_uncertainty_invented": True,
            "no_forbidden_quantity_emitted": True,
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(inventory, indent=2))
    write_yaml(OUT_YAML, PINNED_SHA256, hash_status, fortran, pipeline)

    print(f"OK: {OUT_JSON}")
    print(f"OK: {OUT_YAML}")
    print(f"dependency counts: {fortran['dependency_counts']}")


def write_yaml(out_path: Path, pinned: dict, hash_status: dict, fortran: dict, pipeline: dict) -> None:
    rows = []
    for name, d in fortran["dependencies"].items():
        rows.append(
            f"      {name}:\n"
            f"        classification: {d['classification']}\n"
            f"        library_family: \"{d['library_family']}\"\n"
            f"        call_lines: {d['call_lines'][:20]}"
        )
    dep_block = "\n".join(rows)

    yaml_text = f"""# =============================================================================
# ELLINGSEN 1998/99 PROCESSING-SOFTWARE INVENTORY (machine-readable provenance)
# Produced by scripts/ellingsen_fortran_inventory.py (deterministic; re-runnable).
# Directive: MASTER DIRECTIVE 2026-08-29 sections 11, 12, 28.
# Static analysis ONLY. No missing routine reconstructed. No inference emitted.
# =============================================================================
inventory_version: "1.0"
created_utc: "2026-08-29"
donor: "Simon Ellingsen (relayed via project owner; original email not locally archived)"
frozen_sources:
  fortran:
    path: research/sources/ellingsen_hobart/software/mpslpp.f
    sha256: {pinned['software/mpslpp.f']}
    bytes: {hash_status['software/mpslpp.f'].get('bytes')}
  documentation:
    path: research/sources/ellingsen_hobart/documentation/mpslpp.tex
    sha256: {pinned['documentation/mpslpp.tex']}
    bytes: {hash_status['documentation/mpslpp.tex'].get('bytes')}
program_identity:
  name: MPSLPP
  full_name: "Mt Pleasant Spectral Line Processing Package"
  author: "S P Ellingsen"
  version: "1.8"
  release_date: "19-Jul-1995"
  rcs_id: "$Id: mpslpp.f,v 1.8 1995/03/24 10:33:51 sellings Exp sellings $"
  platforms: [VMS, "PC (Lahey Fortran + Phar Lap 386)"]
structure:
  total_lines: {fortran['total_lines']}
  program_units: {json.dumps(fortran['program_units'])}
  includes: {json.dumps([i['file'] for i in fortran['includes']])}
  common_blocks: {len(fortran['common_blocks'])}
  external_declarations: {json.dumps([e['name'] for e in fortran['external_declarations']])}
  key_parameters: {json.dumps(fortran['parameters_extracted'])}
dependency_map:
  note: >-
    Classifications per directive section 12: FOUND / FOUND_PARTIAL /
    REFERENCED_BUT_MISSING / NOT_REFERENCED / UNKNOWN. No dependency was
    reconstructed or guessed.
  counts: {json.dumps(fortran['dependency_counts'])}
  entries:
{dep_block}
historical_pipeline:
  documented_path: {json.dumps(pipeline['load_path_per_source_lines'], indent=2)}
  reproducibility: {json.dumps(pipeline['reproducibility_status_per_arrow'], indent=2)}
data_interpretation_1998_99:
  correlator_files_contain: "1024-lag autocorrelation functions (source: maxlag=1024 parameter + manual 'store the observations as autocorrelation functions' + archived COUNTS units)"
  spectra_require: "FFT with Van Vleck one-bit correction; Hanning smoothing optional before FFT"
  unresolved: "bandwidth, lag-to-channel mapping, Doppler/frame conventions, executed calibration choices (GAP-HOB-012 tail)"
provenance_locators:
  dependency_map_json: research/sources/ellingsen_hobart/analysis/fortran_dependency_map.json
  hash_manifest: research/sources/ellingsen_hobart/hashes/SIMON_SOFTWARE_SHA256SUMS.txt
  forensic_report: docs/acquisition/HOBART_1998_99_FORENSIC_PROCESSING_REPORT.md
"""
    out_path.write_text(yaml_text)


if __name__ == "__main__":
    main()



