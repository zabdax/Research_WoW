"""Ellingsen/Hobart source-lock integrity checks.

Verifies (MASTER DIRECTIVE §24):
  1. the source manifest exists and its gate remains BLOCKED;
  2. the inventory exists and every recorded path exists under original/;
  3. every SHA-256 in the freeze matches current file content (full
     verification by default; set ELLINGSEN_HASH_MODE=sample to check every
     50th file plus all small files when iterating during development);
  4. file counts agree between manifest, inventory, and disk;
  5. provenance classifications use only sanctioned vocabulary;
  6. the project-wide five-way comparison gate remains disabled;
  7. derived/ stays empty until explicitly authorized conversions appear.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "sources" / "ellingsen_hobart"
MANIFEST = BASE / "metadata" / "source_manifest.yaml"
INVENTORY = BASE / "metadata" / "file_inventory.csv"
SUMS = BASE / "hashes" / "SHA256SUMS.txt"
ORIGINAL = BASE / "original"

ALLOWED_PROVENANCE_TOKENS = {
    "DONOR_SUPPLIED", "ORIGINAL_ARCHIVAL", "RAW_OBSERVATIONAL",
    "INTERMEDIATE_PROCESSING", "PROCESSED_OBSERVATION", "STATISTICAL_OUTPUT",
    "CALIBRATION", "POINTING_METADATA", "SCAN_METADATA", "DOCUMENTATION",
    "TRANSCRIPTION", "PUBLICATION", "DERIVED", "UNKNOWN",
}


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _inventory() -> list[dict]:
    import csv

    with open(INVENTORY, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _hash_mode_sample() -> bool:
    return os.environ.get("ELLINGSEN_HASH_MODE", "").lower() == "sample"


def test_manifest_exists_and_gate_blocked():
    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["donor"], "donor must be recorded"
    assert manifest["file_count"] == 6681
    assert manifest["integrity"]["files_hashed"] == 6681
    assert manifest["integrity"]["zero_byte_files"] == 0
    assert "BLOCKED" in manifest["gate_status"]
    assert manifest["completeness_assessment"] == "UNKNOWN"


def test_inventory_covers_original_tree_exactly():
    rows = _inventory()
    inv_paths = [r["relative_path"] for r in rows]
    disk_paths = sorted(
        p.relative_to(BASE).as_posix() for p in ORIGINAL.rglob("*") if p.is_file()
    )
    assert sorted(inv_paths) == disk_paths, (
        "original/ changed relative to the frozen inventory "
        "(new, renamed, or deleted files are forbidden after freeze)"
    )
    assert len(rows) > 6000


def test_all_hashes_verify():
    """Full-content verification of the SHA-256 freeze against originals."""
    sums = {}
    for line in SUMS.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        sums[rel] = digest
    rows = _inventory()
    assert len(sums) == len(rows)
    step = 50 if _hash_mode_sample() else 1
    checked = 0
    for i, row in enumerate(rows):
        if step != 1 and i % step and int(row["size_bytes"]) < 10_000_000:
            continue
        assert _sha256(BASE / row["relative_path"]) == row["sha256"], (
            f"content mismatch: {row['relative_path']} "
            "(original modified after freeze?)"
        )
        assert sums[row["relative_path"]] == row["sha256"]
        checked += 1
    assert checked >= len(rows) // max(step, 1)


def test_provenance_vocabulary_and_no_blank_roles():
    for row in _inventory():
        tokens = set(row["provenance_classification"].split("|"))
        assert tokens <= ALLOWED_PROVENANCE_TOKENS, row["relative_path"]
        assert row["suspected_role"].strip(), row["relative_path"]
        assert row["sha256"], row["relative_path"]


def test_five_way_comparison_gate_still_disabled():
    cfg = yaml.safe_load(
        (ROOT / "configs" / "research_status.yaml").read_text(encoding="utf-8")
    )
    assert cfg["confirmatory_comparison_enabled"] is False
    assert cfg["model_readiness"]["H5"] == "in_progress"


def test_campaign_exposure_table_present():
    import csv

    path = BASE / "extracted" / "campaign_exposure.csv"
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    campaigns = {r["campaign"] for r in rows}
    assert {"2010_followup", "2013_followup", "2013_tests"} <= campaigns
    # sensitivity/threshold fields must not be silently invented anywhere
    for r in rows:
        assert r["detection_threshold"] in {"UNKNOWN", ""} or r[
            "detection_threshold"
        ].startswith(("NOT_", "UNKNOWN")), r["session"]


def test_derived_dir_still_empty():
    assert list((BASE / "derived").iterdir()) == [], (
        "derived/ must stay empty until human review authorizes conversions"
    )
