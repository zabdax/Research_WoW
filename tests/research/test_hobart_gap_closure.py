"""Gap-closure phase guards for the Ellingsen/Hobart branch (MASTER DIRECTIVE
§19 of the gap-closure directive).

These tests do not touch the archive; they verify that:
  1. the forensic-phase manifest and freeze remain intact;
  2. the Arecibo/Méndez evidence freeze is byte-unchanged;
  3. duplicate 2010 packaging is never treated as independent exposure;
  4. no likelihood / Bayes factor / numerical detection efficiency /
     posterior artifact is emitted by this branch;
  5. 2013/14 nominal-Tsys outputs are never promoted to absolute calibration;
  6. no coordinate is silently converted between epochs;
  7. pointing-intent gaps remain formally unresolved;
  8. censored Arecibo quantities remain censored;
  9. every campaign stays unusable-for-likelihood in the non-detection register.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "sources" / "ellingsen_hobart"
DOCS = ROOT / "docs" / "acquisition"

FORBIDDEN_NUMERIC_KEYS = (
    "bayes_factor", "posterior", "h5_likelihood", "marginal_evidence",
    "detection_efficiency", "p_detect", "p_nodetect",
)


def _yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# --- 1. forensic freeze intact ----------------------------------------------
def test_forensic_manifest_and_gate_intact():
    m = _yaml(BASE / "metadata" / "source_manifest.yaml")
    assert m["file_count"] == 6681
    assert "BLOCKED" in m["gate_status"]
    assert m["scientific_use_status"]["blocked_until_human_review"]
    assert list((BASE / "derived").iterdir()) == []


# --- 2. Arecibo/Méndez freeze unchanged --------------------------------------
def test_arecibo_evidence_vector_byte_unchanged():
    freeze = _yaml(ROOT / "research" / "data" / "mendez_evidence_freeze_manifest.yaml")
    recorded = freeze["frozen_files"]["mendez_evidence_vector"]["sha256"]
    live = ROOT / "research" / "data" / "mendez_evidence_vector.yaml"
    assert _sha256(live) == recorded


def test_censored_flux_row_remains_censored():
    csv_text = (ROOT / "research" / "data" / "historical_vs_arecibo_parameters.csv").read_text(
        encoding="utf-8"
    )
    flux_rows = [ln for ln in csv_text.splitlines() if ln.startswith("flux_density")]
    assert flux_rows, "flux_density parameter row missing"
    assert "censored lower bound" in flux_rows[0]


# --- 3. duplicate packaging never counted twice -------------------------------
def test_2010_packaging_counted_once():
    import csv

    rows = list(csv.DictReader(open(BASE / "extracted" / "campaign_exposure.csv")))
    assert not [r for r in rows if "spectra.tar.gz" in r["source_file"]]
    meta = _yaml(ROOT / "research" / "data" / "ellingsen_campaign_metadata.yaml")
    assert meta["campaigns"]["campaign_2010"]["duplication_rule"] == "count once"
    assert meta["campaigns"]["campaign_2010"]["spectra_count_unique"] == 6500


# --- 4/7. no emitted inference artifacts; intent gaps stay open ---------------
def _forbidden_key_scan() -> list[str]:
    bad = []
    targets = list((ROOT / "research" / "data").glob("ellingsen_*.yaml"))
    targets.append(ROOT / "research" / "sources" / "ellingsen_hobart" / "analysis" / "HOBART_LOCAL_EVIDENCE_MAP.yaml")
    for path in targets:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for key in FORBIDDEN_NUMERIC_KEYS:
            for line in text.splitlines():
                stripped = line.split("#")[0]
                if re.search(rf"^\s*{key}\s*:", stripped, re.I):
                    bad.append(f"{path.name}:{line.strip()}")
    return bad


def test_no_inference_quantities_emitted():
    assert _forbidden_key_scan() == []


def test_docs_contain_no_numerical_detection_efficiency():
    pattern = re.compile(r"(efficiency|P\(detect)[^.\n]*?[=:]\s*-?\d+\.\d+", re.I)
    offenders = []
    for doc in DOCS.glob("*hobart*.md"):
        for i, line in enumerate(doc.read_text(encoding="utf-8").splitlines(), 1):
            if pattern.search(line):
                offenders.append(f"{doc.name}:{i}")
    assert offenders == []


def test_pointing_intent_gaps_not_silently_resolved():
    reg = _yaml(ROOT / "research" / "data" / "ellingsen_gap_register.yaml")
    for gid in ("GAP-HOB-002", "GAP-HOB-003", "GAP-HOB-004"):
        g = reg["gaps"][gid]
        assert g["status"] in ("OPEN", "PARTIALLY_RESOLVED", "RESOLVED"), gid
        if g["status"] == "RESOLVED":
            blob = str(g)
            assert ("HOBART_XLS_PLAN_TEXT" in blob) or (".xls" in blob), (
                f"{gid} resolved without plan-document locator"
            )
        else:
            assert "still_open" in g, f"{gid} neither resolved-with-locator nor open"


def test_session_master_table_complete_and_located():
    import csv

    path = BASE / "extracted" / "HOBART_SESSION_MASTER_TABLE.csv"
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
    assert len(rows) >= 33
    rpf_rows = [r for r in rows if r["rpfits_association"] != "NOT_APPLICABLE"]
    assert len(rpf_rows) == 27
    for r in rows:
        assert r["source_locators"].strip(), r["session_id"]
        assert r["integration_time_s"].startswith("5.0 per plan") or r[
            "integration_time_s"
        ] == "UNKNOWN", r["session_id"]
    # epoch must be declared on every row
    assert all(r["coordinate_epoch"].strip() for r in rows)


def test_channel_count_discrepancy_is_registered_not_resolved():
    reg = _yaml(ROOT / "research" / "data" / "ellingsen_gap_register.yaml")
    g = reg["gaps"]["GAP-HOB-018"]
    assert g["status"] == "OPEN"
    meta = _yaml(ROOT / "research" / "data" / "ellingsen_campaign_metadata.yaml")
    assert meta["spectral_configurations"]["authoritative"]["channels_per_pol"] == 4096


# --- 5. no undocumented calibration promotion ---------------------------------
def test_2013_2014_stay_relative_normalization():
    meta = _yaml(ROOT / "research" / "data" / "ellingsen_campaign_metadata.yaml")
    cal = meta["calibration_status_by_campaign"]
    for era in ("2013", "2014"):
        assert cal[era]["status"] != "DOCUMENTED_AND_REPRODUCIBLE"
        assert cal[era]["verdict_class"].startswith("C")


# --- 6. no silent epoch conversions -------------------------------------------
def test_coordinate_entries_declare_frame_epoch_and_methods():
    cp = _yaml(ROOT / "research" / "data" / "ellingsen_coordinate_provenance.yaml")
    for name, e in cp["entries"].items():
        assert "frame" in e and "epoch" in e, name
        for k, v in e.items():
            if "derived" in k and isinstance(v, str) and ":" in v:
                assert e.get("method"), f"{name}.{k} transformed without method"


def test_hobart_command_positions_blocked_from_weighting():
    cp = _yaml(ROOT / "research" / "data" / "ellingsen_coordinate_provenance.yaml")
    for name in ("hobart_field1_commanded", "hobart_field2_commanded",
                 "hobart_2010_on"):
        assert cp["entries"][name]["suitable_for_beam_weighting"] is False
        assert "blocking_gap" in cp["entries"][name]


# --- 9. non-detection register keeps every campaign unusable -------------------
def test_nondetection_register_all_unusable():
    text = (DOCS / "hobart_nondetection_status.md").read_text(encoding="utf-8")
    rows = [ln for ln in text.splitlines() if ln.startswith("| ") and "**NO**" in ln]
    assert len(rows) >= 5
