"""Phase 0 source-lock integrity checks for the Méndez/Arecibo evidence freeze.

Verifies (MASTER DIRECTIVE §0.14):
  1. required source files exist locally;
  2. required repository commits are recorded;
  3. hashes match the source manifest;
  4. the frozen paper version is unambiguous;
  5. the Wow! flux remains a censored lower bound, never a point estimate.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "research" / "sources" / "mendez_arecibo" / "metadata" / "source_manifest.yaml"


def _load_manifest() -> dict:
    return yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_manifest_exists_and_declares_gate():
    manifest = _load_manifest()
    assert manifest["manifest_version"]
    # Phase A must remain blocked until human sign-off is recorded in writing.
    assert "BLOCKED" in manifest["gate_status"]


def test_required_paper_artifacts_exist_and_hash_match():
    manifest = _load_manifest()
    awow2 = manifest["papers"]["awow2_2508.10657"]
    assert awow2["frozen_version"] == "v1", "frozen Arecibo Wow! II version must be pinned"
    for name, artifact in awow2["artifacts"].items():
        path = ROOT / artifact["local_path"]
        assert path.exists(), f"missing frozen artifact: {name} at {artifact['local_path']}"
        assert _sha256(path) == artifact["sha256"], f"hash mismatch for {name}"


def test_companion_paper_artifacts_hash_match():
    manifest = _load_manifest()
    for key in ("awow1_2408.08513", "ohio_seti_last_decades_2606.11102"):
        for artifact in manifest["papers"][key]["artifacts"].values():
            path = ROOT / artifact["local_path"]
            assert path.exists(), f"missing frozen artifact: {artifact['local_path']}"
            assert _sha256(path) == artifact["sha256"], f"hash mismatch for {artifact['local_path']}"


def test_repository_commits_recorded_and_local_heads_match():
    import subprocess

    manifest = _load_manifest()
    for key in ("ohio_seti", "hotaling_transcription"):
        repo = manifest["repositories"][key]
        assert repo["commit"], f"{key}: commit SHA must be recorded"
        # Local clone lives under the frozen repositories/ workspace.
        expected_names = {"ohio_seti": "Ohio-SETI", "hotaling_transcription": "The-Wow-Signal"}
        clone = ROOT / "research" / "sources" / "mendez_arecibo" / "repositories" / expected_names[key]
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=clone, text=True).strip()
        assert head == repo["commit"], f"{key}: local HEAD {head} != recorded {repo['commit']}"


def test_ohio_seti_data_files_hash_match():
    manifest = _load_manifest()
    files = manifest["repositories"]["ohio_seti"]["files"]
    assert len(files) == 6
    base = ROOT / "research" / "sources" / "mendez_arecibo" / "repositories" / "Ohio-SETI"
    for name, record in files.items():
        path = base / name
        assert path.exists(), f"missing Ohio-SETI file: {name}"
        assert _sha256(path) == record["sha256"], f"hash mismatch for Ohio-SETI/{name}"


def test_arxiv_version_and_journal_checks_are_dated():
    manifest = _load_manifest()
    awow2 = manifest["papers"]["awow2_2508.10657"]
    version_check = awow2["version_check"]
    apj_check = awow2["apj_status_check"]
    assert version_check["checked_utc"].startswith("2026-08-22")
    assert apj_check["checked_utc"].startswith("2026-08-22")
    assert "result" in version_check and "result" in apj_check


def test_wow_flux_remains_censored_lower_bound():
    observation = yaml.safe_load((ROOT / "research" / "data" / "wow_observation.yaml").read_text(encoding="utf-8"))
    flux = observation["event"]["flux_density"]
    assert flux["kind"] == "lower_bound", "flux lower bound must never silently become a point estimate"
