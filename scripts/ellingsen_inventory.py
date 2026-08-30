"""Read-only forensic inventory of the Ellingsen/Hobart source archive.

Walks research/sources/ellingsen_hobart/original/, computes SHA-256 for every
file, sniffs formats from content signatures, applies rule-based provisional
provenance classifications, detects duplicates and anomalies, and writes:

    research/sources/ellingsen_hobart/metadata/file_inventory.csv
    research/sources/ellingsen_hobart/metadata/inventory_summary.json
    research/sources/ellingsen_hobart/hashes/SHA256SUMS.txt

The tool never writes to, renames, or otherwise modifies anything under
original/. Re-running it against an unchanged archive must produce identical
outputs (sorted paths, stable column order).
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE = REPO_ROOT / "research" / "sources" / "ellingsen_hobart"
ORIGINAL = BASE / "original"

CHUNK = 1024 * 1024

# ---------------------------------------------------------------------------
# Content signature sniffing
# ---------------------------------------------------------------------------


def sniff(path: Path) -> tuple[str, str]:
    """Return (detected_type, parser_used) purely from content."""
    size = path.stat().st_size
    if size == 0:
        return ("zero_byte", "stat")
    try:
        with open(path, "rb") as fh:
            head = fh.read(64)
    except OSError as exc:  # unreadable
        return (f"unreadable: {exc}", "open")

    if head.startswith(b"\x1f\x8b"):
        inner = _sniff_gzip(path)
        return (inner, "gzip+zcat-prefix")

    if head.startswith(b"%!PS-Adobe"):
        return ("postscript", "signature")

    if head.startswith(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"):
        return ("ole2_compound_document", "signature")

    if head.startswith(b"%PDF"):
        return ("pdf", "signature")

    if head.lstrip().startswith(b"SIMPLE"):
        # FITS-family signature; distinguish conformant vs NONCONFORMIST RPFITS
        probe = head + b" " * 512
        try:
            with open(path, "rb") as fh:
                probe = fh.read(600)
        except OSError:
            pass
        if b"NONCONFORMIST" in probe:
            return ("rpfits_nonstandard_fits_like", "header-sniff")
        if b"SIMPLE=T" in probe.replace(b" ", b""):
            return ("fits_signature_conformant", "header-sniff")
        return ("fits_signature_present", "header-sniff")

    if head.startswith(b"PK\x03\x04"):
        return ("zip", "signature")

    if head.startswith(b"\x09\x00\x08\x00") or head.startswith(b"\x09\x02\x06\x00"):
        return ("xls_biff_probable", "signature")

    # textual?
    sample = head[:64]
    if all(b == 0x09 or b == 0x0A or b == 0x0D or 0x20 <= b < 0xFF for b in sample):
        return ("text_probable", "heuristic")
    return ("binary_unknown", "fallback")


def _sniff_gzip(path: Path) -> str:
    """Peek at the decompressed prefix of a gzip member."""
    try:
        with gzip.open(path, "rb") as fh:
            prefix = fh.read(600)
    except Exception as exc:
        return f"gzip_unreadable_inner ({exc.__class__.__name__})"
    stripped = prefix.lstrip()
    if prefix.startswith(b"%!PS-Adobe"):
        return "gzip(postscript)"
    if stripped.startswith(b"./") or stripped.startswith(b"2013DOY") or (
        b"\x00" not in prefix[:100] and b"/" in prefix[:100]
    ):
        # crude tar detection: tar members begin with member name text
        if prefix[:100].rstrip(b"\x00").decode("ascii", "replace").strip("./").replace(
            ".", ""
        ).replace("_", "").isalnum():
            return "gzip(tar)"
    if stripped.startswith(b"SIMPLE"):
        return "gzip(fits)"
    return "gzip(unknown-inner)"


# ---------------------------------------------------------------------------
# Provisional provenance rules (automated heuristics; refined manually later)
# ---------------------------------------------------------------------------

ROLE_RULES = [
    ("/data/", ".fit.gz", "1998-99 UTAS correlator FITS spectrum (gzipped)",
     "RAW_OBSERVATIONAL|DONOR_SUPPLIED"),
    (".rpf", "", "RPFITS raw correlator archive",
     "RAW_OBSERVATIONAL|DONOR_SUPPLIED"),
    ("/2010obs/", ".txt", "ASAP-exported calibrated spectrum ASCII dump",
     "PROCESSED_OBSERVATION|DONOR_SUPPLIED"),
    ("/positions/", ".txt", "telescope live-pages position extract",
     "POINTING_METADATA|DONOR_SUPPLIED"),
    ("bruce_", ".log", "observing system log",
     "SCAN_METADATA|DONOR_SUPPLIED"),
    ("ricky_", ".log", "observing system log",
     "SCAN_METADATA|DONOR_SUPPLIED"),
    ("", ".log", "log file", "SCAN_METADATA|DONOR_SUPPLIED"),
    ("", ".gsf.gz", "SAS/GRAPH statistical plot (PostScript)",
     "STATISTICAL_OUTPUT|DONOR_SUPPLIED"),
    ("", ".py", "ASAP reduction/extraction script",
     "INTERMEDIATE_PROCESSING|DONOR_SUPPLIED"),
    ("", ".tar.gz", "donor-packaged bundle of processed spectra",
     "PROCESSED_OBSERVATION|DONOR_SUPPLIED"),
    ("", ".xls", "observing plan spreadsheet",
     "DOCUMENTATION|SCAN_METADATA|DONOR_SUPPLIED"),
    ("", ".pdf", "published paper", "PUBLICATION|DONOR_SUPPLIED"),
    ("README", "", "campaign documentation", "DOCUMENTATION|DONOR_SUPPLIED"),
    ("", ".fit", "single uncompressed FITS product (role pending forensics)",
     "UNKNOWN|DONOR_SUPPLIED"),
]


def classify(relpath: str, detected: str) -> tuple[str, str]:
    lowered = relpath.lower()
    for needle, ext, role, prov in ROLE_RULES:
        if needle and needle.lower() not in lowered:
            continue
        if ext and not lowered.endswith(ext):
            continue
        return role, prov
    if detected.startswith("text"):
        return "text file (role undetermined)", "UNKNOWN|DONOR_SUPPLIED"
    return "unclassified", "UNKNOWN|DONOR_SUPPLIED"


def main() -> int:
    if not ORIGINAL.is_dir():
        print(f"FATAL: {ORIGINAL} missing", file=sys.stderr)
        return 2

    started = datetime.now(timezone.utc)
    rows = []
    seen_hashes: dict[str, str] = {}
    ext_counts: dict[str, int] = {}
    zero_byte = []
    duplicates = []
    total_bytes = 0

    files = sorted(p for p in ORIGINAL.rglob("*") if p.is_file())
    n = len(files)
    print(f"[inventory] {n} files under {ORIGINAL}", flush=True)

    for i, path in enumerate(files, 1):
        rel = path.relative_to(BASE).as_posix()
        st = path.stat()
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            while True:
                chunk = fh.read(CHUNK)
                if not chunk:
                    break
                h.update(chunk)
        digest = h.hexdigest()

        dup_of = seen_hashes.get(digest, "")
        if dup_of:
            duplicates.append((rel, dup_of))
        else:
            seen_hashes[digest] = rel

        detected, parser = sniff(path)
        ext = path.suffix.lower().lstrip(".") or "[noext]"
        ext_counts[ext] = ext_counts.get(ext, 0) + 1
        role, prov = classify(rel, detected)

        mtime = datetime.fromtimestamp(st.st_mtime, tz=timezone.utc)
        notes = []
        if st.st_size == 0:
            zero_byte.append(rel)
            notes.append("ZERO-BYTE")
        if path.name == ".DS_Store":
            notes.append("macOS Finder metadata artifact")
        if dup_of:
            notes.append(f"exact duplicate of {dup_of}")
        if mtime.year == 2026:
            notes.append("mtime reflects 2026 transfer, not acquisition epoch")

        rows.append(
            {
                "relative_path": rel,
                "filename": path.name,
                "extension": ext,
                "size_bytes": st.st_size,
                "mtime_utc": mtime.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "sha256": digest,
                "mime_detected": detected,
                "suspected_role": role,
                "provenance_classification": prov,
                "readability": "readable" if not detected.startswith("unreadable") else "unreadable",
                "parser_used": parser,
                "notes": "; ".join(notes),
                "duplicate_of": dup_of,
                "relationship_notes": "",
            }
        )
        total_bytes += st.st_size
        if i % 500 == 0:
            print(f"[inventory] {i}/{n}", flush=True)

    finished = datetime.now(timezone.utc)

    # ---- outputs -----------------------------------------------------------
    inv_path = BASE / "metadata" / "file_inventory.csv"
    inv_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "relative_path", "filename", "extension", "size_bytes", "mtime_utc",
        "sha256", "mime_detected", "suspected_role", "provenance_classification",
        "readability", "parser_used", "notes", "duplicate_of", "relationship_notes",
    ]
    with open(inv_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    sums_path = BASE / "hashes" / "SHA256SUMS.txt"
    sums_path.parent.mkdir(parents=True, exist_ok=True)
    with open(sums_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# Ellingsen/Hobart source freeze\n")
        fh.write(f"# generated_utc={started.strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
        fh.write("# format: SHA256  <relpath relative to research/sources/ellingsen_hobart/>\n")
        for row in rows:
            fh.write(f"{row['sha256']}  {row['relative_path']}\n")

    summary = {
        "generated_utc": started.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "completed_utc": finished.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tool": "scripts/ellingsen_inventory.py",
        "python": platform.python_version(),
        "platform": platform.platform(),
        "root": "research/sources/ellingsen_hobart/original",
        "file_count": len(rows),
        "total_bytes": total_bytes,
        "unique_sha256_count": len(seen_hashes),
        "duplicate_pair_count": len(duplicates),
        "zero_byte_files": zero_byte,
        "extension_counts": dict(sorted(ext_counts.items(), key=lambda kv: -kv[1])),
        "duplicates": [{"path": a, "duplicate_of": b} for a, b in duplicates],
        "notes": [
            "mtimes are 2026 download-time artifacts; acquisition dating relies on embedded headers, logs, and documentation",
            "provenance_classification values are provisional automated heuristics pending manual review",
        ],
    }
    with open(BASE / "metadata" / "inventory_summary.json", "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2)

    print(
        f"[inventory] DONE files={len(rows)} bytes={total_bytes} "
        f"unique_hashes={len(seen_hashes)} duplicates={len(duplicates)} "
        f"zero_byte={len(zero_byte)}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
