"""Phase A evidence-vector integrity checks (post-freeze).

Verifies (authorization Part 3 / MASTER DIRECTIVE §0.14):
  - frozen vector + comparison CSV match the freeze-manifest hashes;
  - flux is censored, never a point estimate;
  - abstract and commented-out TeX draft values never appear as values;
  - key parameters carry full provenance locators;
  - reproduction results carry the mandated verification-mode labels.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
VECTOR_PATH = ROOT / "research" / "data" / "mendez_evidence_vector.yaml"
CSV_PATH = ROOT / "research" / "data" / "historical_vs_arecibo_parameters.csv"
FREEZE_PATH = ROOT / "research" / "data" / "mendez_evidence_freeze_manifest.yaml"
RESULTS_PATH = ROOT / "research" / "data" / "processed" / "mendez_reproduction_results.json"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _vector() -> dict:
    return yaml.safe_load(VECTOR_PATH.read_text(encoding="utf-8"))


def test_frozen_files_match_freeze_manifest_hashes():
    freeze = yaml.safe_load(FREEZE_PATH.read_text(encoding="utf-8"))
    for entry in freeze["frozen_files"].values():
        path = ROOT / entry["path"]
        assert path.exists(), f"missing frozen file {entry['path']}"
        assert _sha256(path) == entry["sha256"], f"hash mismatch for {entry['path']}"
    for entry in freeze["post_freeze_phase_c_artifacts"].values():
        assert _sha256(ROOT / entry["path"]) == entry["sha256"]


def test_vector_is_frozen_and_authorized():
    vector = _vector()
    assert vector["frozen"]["status"] == "FROZEN"
    assert vector["frozen"]["date_utc"] == "2026-08-23"


def test_flux_remains_censored_lower_bound():
    flux = _vector()["parameters"]["flux_density"]
    assert flux["kind"] == "lower_bound_censored"
    assert flux["bound_value_jy"] == 256 and flux["uncertainty_jy"] == 63
    assert "ambiguity_preserved" in flux["censoring_semantics"]
    assert "point" not in flux["kind"]


def test_excluded_values_do_not_appear_as_values():
    text = VECTOR_PATH.read_text(encoding="utf-8")
    # The excluded-value DOCUMENTATION may mention them; value fields may not.
    vector = _vector()
    assert vector["parameters"]["flux_density"]["bound_value_jy"] != 249
    assert vector["parameters"]["flux_density"]["bound_value_jy"] != 250
    assert "distance" not in _vector()["parameters"]
    assert all("1.5 +/- 1.4" not in str(v) for v in vector["parameters"].values())


def test_core_parameters_carry_provenance_locators():
    params = _vector()["parameters"]
    for key in ("observed_frequency", "flux_density", "position_J2000", "radial_velocity_lsr", "snr_peak", "signal_apparent_duration"):
        block = params[key]
        source = block["source"]
        assert any(k in source for k in ("table", "section", "equation", "figure")), f"{key} lacks locator"
        assert block["provenance_class"], f"{key} lacks provenance class"
    freq = params["observed_frequency"]
    assert freq["source"]["table"].startswith("Table 4")
    assert freq["underlying_data"]["commit"].startswith("28624a1")


def test_hi_wow23_tagged_paper_only():
    block = _vector()["parameters"]["hi_wow23"]
    assert block["SOURCE_VERIFICATION"] == "PAPER_ONLY__NOT_INDEPENDENTLY_REPRODUCIBLE"
    assert "2027" in block["signer_condition"]


def test_comparison_csv_columns_and_flux_row():
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = {"parameter", "legacy_project_value", "Ohio_SETI_value", "Arecibo_II_value", "status", "scientific_consequence"}
    assert required <= set(rows[0].keys())
    flux_row = next(r for r in rows if r["parameter"] == "flux_density")
    assert "256" in flux_row["Arecibo_II_value"]
    assert flux_row["status"] == "CHANGED"
    legacy_flux_row = next(r for r in rows if r["parameter"] == "flux_calibration_legacy_row")
    assert legacy_flux_row["status"] == "LEGACY_CALIBRATION"


def test_reproduction_results_labels_and_outcomes():
    results = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
    freq = results["frequency_chain"]
    assert freq["mode"] == "GENUINE_INDEPENDENT_VERIFICATION"
    assert freq["status"] == "AGREE"
    assert results["frequency_data_level_check"]["match"] is True
    assert results["frequency_data_level_check"]["sequence_match"] is True
    flux = results["flux_arithmetic"]
    assert flux["mode"] == "ARITHMETIC_REPRODUCTION_ONLY"
    assert flux["our_reproduction_of_paper_path"]["status"].startswith("MATCH")
    assert "rounding-policy artifact" in flux["unrounded_propagation_finding"]["finding"]
    galactic = results["galactic_consistency_check"]
    assert galactic["mode"] == "INTERNAL_CONSISTENCY_CHECK_REPORT_ONLY"
    assert abs(galactic["positive_horn_delta"]["b_deg"] - 1.04) < 1e-9


def test_galactic_status_confirmed_typo_with_independent_verification():
    galactic = _vector()["parameters"]["position_galactic"]
    assert galactic["status"] == "CONFIRMED_TYPO_INDEPENDENTLY_VERIFIED"
    verif = galactic["independent_verification_2026_08_23"]
    assert abs(verif["computed_positive_horn_b_deg"] - (-18.8181)) < 1e-4
    assert abs(verif["printed_value_disagreement_deg"] - 0.9681) < 1e-3
    assert "author confirmation" in verif["confidence"]
    # The printed -17.85 must never be the value downstream code would use.
    assert "-17.85" not in str(galactic["usage_rule"]).replace("NEVER the printed -17.85", "")


def test_censoring_semantics_is_full_prose():
    semantics = _vector()["parameters"]["flux_density"]["censoring_semantics"]
    prose = semantics["description"]
    # All three required points must be present as explanatory sentences.
    assert "lower limit" in prose and "no formal statistical definition" in prose
    assert "beam" in prose and "likely greater" in prose
    assert "approximately double" in prose
    assert len(prose) > 500, "censoring description must be referee-readable prose, not a tag"


def test_flux_rounding_sensitivity_note_present_and_neutral():
    note = _vector()["parameters"]["flux_density"]["rounding_sensitivity_note"]
    assert "250.1" in note and "256" in note
    assert "1.175" in note
    assert "not privileged" in note or "neither value is privileged" in note


def test_galactic_verification_results_exist_and_agree_with_vector():
    path = ROOT / "research" / "data" / "processed" / "galactic_verification_results.json"
    results = json.loads(path.read_text(encoding="utf-8"))
    row = results["rows"]["new_positive"]
    assert abs(row["computed_b_deg"] - (-18.8181)) < 1e-4
    assert abs(row["delta_b_printed_minus_computed_deg"] - 0.9681) < 1e-3
    for key in ("previous_positive", "new_negative", "previous_negative"):
        assert abs(results["rows"][key]["delta_b_printed_minus_computed_deg"]) < 0.05, f"{key} should validate to <0.05 deg"
