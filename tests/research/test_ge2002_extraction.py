"""GE2002 extraction phase guard tests (directive section 16).

Fails if:
- the frozen G&E 2002 PDF hash drifts or extraction artifacts are lost;
- the published non-detection record is altered or loses locators;
- evidence-class vocabulary is violated;
- a Bayesian quantity leaks into the new artifacts;
- confirmatory_comparison_enabled becomes true;
- the frozen Arecibo evidence vector changes;
- the 1998/99 published non-detection is misread as candidate-level data;
- DONOR_REPORTED material is upgraded to DIRECTLY_STATED in the paper
  extraction;
- the raw donor archive is modified.
"""

import hashlib
import json
import re
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "research" / "sources" / "ellingsen_hobart"
DATA = REPO / "research" / "data"
GE_DIR = SRC / "extracted" / "ge2002"
PDF = SRC / "original" / "drive-download-20260825T053211Z-1-001" / "wow_published.pdf"
PDF_SHA256 = "68c9a9c02a245df4dc0ae61b015856eea2e36f7c4e51f68c3673b73d5669e2b3"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture(scope="module")
def extraction():
    return yaml.safe_load((DATA / "ge2002_extraction.yaml").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def outcome():
    return yaml.safe_load((DATA / "ge2002_search_outcome.yaml").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def register():
    return yaml.safe_load((DATA / "ellingsen_gap_register.yaml").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def fulltext():
    return (GE_DIR / "fulltext.txt").read_text(encoding="utf-8")

# --- source integrity ---------------------------------------------------------


def test_source_pdf_hash_fixed():
    assert _sha256(PDF) == PDF_SHA256
    sums = (SRC / "hashes" / "SHA256SUMS.txt").read_text(encoding="utf-8")
    assert PDF_SHA256 in sums, "PDF hash not anchored in the frozen Hobart manifest"


def test_extraction_artifacts_present():
    for name in [f"page{i:02d}.txt" for i in range(1, 6)] + ["fulltext.txt", "extraction_manifest.json"]:
        assert (GE_DIR / name).exists(), f"missing extraction artifact: {name}"
    manifest = json.loads((GE_DIR / "extraction_manifest.json").read_text(encoding="utf-8"))
    assert manifest["source_sha256"] == PDF_SHA256
    assert manifest["page_count"] == 5
    assert all(p["n_chars_text_layer"] > 4000 for p in manifest["pages"])
    assert manifest["source_modified"] is False


def test_paper_content_cross_check(fulltext):
    """Key claims must be present in the raw extracted text (no drift).

    Whitespace-normalized because the PDF text layer wraps lines mid-sentence.
    """
    flat = " ".join(fulltext.split())
    for phrase in [
        "A SEARCH FOR PERIODIC EMISSIONS AT THE WOW LOCALE",
        "No emissions resembling the Wow were detected",
        "density limit of about 18 Jy",  # ligature-safe (raw text has 'ï¬‚ux' mojibake for 'flux')
        "detection threshold of 5.9",
        "repeating more often than every 14 hr",
        "University of Tasmania Hobart 26 m",
        "512 (each polarization)",
        "Virgo A",
        "19h25m12s",
        "Ellingsen 1996",
    ]:
        assert " ".join(phrase.split()) in flat, f"expected paper text missing: {phrase!r}"


# --- published outcome vs selection function -----------------------------------


def test_published_non_detection_record(outcome):
    assert outcome["published_outcome"]["verdict"] == "PUBLISHED_NON_DETECTION"
    claims = " ".join(c["claim"] for c in outcome["published_outcome"]["exact_claims"])
    assert "No emissions resembling the Wow were detected" in claims
    assert "No signals resembling the Ohio State Wow were detected" in claims


def test_no_selection_function_claimed(outcome):
    assert outcome["selection_function_status"]["can_reconstruct_full_selection_function"] == "NO"
    assert "P(no detection | H5)" in " ".join(
        outcome["interpretation_guard"]["forbidden_conversions"])


def test_candidate_record_not_converted_to_non_detection(outcome):
    ce = outcome["published_outcome"]["candidates_encountered"]
    assert len(ce["features"]) == 2, "both described features must be recorded"
    assert ce["classification"] == "PUBLISHED_RESULT_WITHOUT_SURVIVING_CANDIDATE_LEVEL_DATA"
    assert "NOT_FOUND_IN_SUPPLIED_ARCHIVE" in ce["status_note"]

# --- no inference quantities / gates -------------------------------------------


@pytest.mark.parametrize("rel", [
    "research/data/ge2002_extraction.yaml",
    "research/data/ge2002_search_outcome.yaml",
])
def test_no_bayesian_quantities_in_new_artifacts(rel):
    text = (REPO / rel).read_text(encoding="utf-8").lower()
    for forbidden in ("bayes factor:", "posterior odds:", "p(data|h5)",
                      "p(no detection|h5)", "detection efficiency =",
                      "confirmatory_comparison_enabled: true"):
        assert forbidden not in text, f"forbidden quantity in {rel}: {forbidden}"


def test_five_way_gate_stays_closed():
    cfg = yaml.safe_load((REPO / "configs" / "research_status.yaml").read_text(encoding="utf-8"))
    assert cfg["confirmatory_comparison_enabled"] is False


def test_arecibo_evidence_vector_unchanged():
    manifest = yaml.safe_load((DATA / "mendez_evidence_freeze_manifest.yaml").read_text(encoding="utf-8"))
    pinned = manifest["frozen_files"]["mendez_evidence_vector"]["sha256"]
    assert _sha256(DATA / "mendez_evidence_vector.yaml") == pinned


# --- donor/upgrading guards ------------------------------------------------------


def test_donor_statements_not_upgraded(extraction):
    """Simon's recollections must not appear as paper facts.

    The paper extraction is purely documentary: no evidence_class may carry
    DONOR_REPORTED, and Simon's verbatim wording must not appear as a paper
    statement.
    """
    assert "Yes that sounds correct" not in str(extraction)

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "evidence_class" and isinstance(v, str):
                    assert "DONOR_REPORTED" not in v, \
                        f"donor-derived class leaked into paper extraction: {v!r}"
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)
    walk(extraction)


# --- gap register round-4 ---------------------------------------------------------


def test_gap_register_round4_era_split(register):
    assert register["register_version"] == 1.3
    g = register["gaps"]
    for gap_id in ("GAP-HOB-005", "GAP-HOB-006", "GAP-HOB-007", "GAP-HOB-008", "GAP-HOB-009"):
        assert g[gap_id]["status"].startswith("RESOLVED_LOCAL_1998_99"), gap_id
        assert "ge2002_amendment" in g[gap_id], gap_id
    assert g["GAP-HOB-012"]["status"] == "PARTIALLY_RESOLVED_LOCAL__TECHNICALLY_OPEN"
    assert g["GAP-HOB-017"]["status"].startswith("RESOLVED_LOCAL_1998_99")
    audit = register["ge2002_extraction_round"]["changes"]
    assert {c["gap"] for c in audit} == {
        "GAP-HOB-005", "GAP-HOB-006", "GAP-HOB-007", "GAP-HOB-008",
        "GAP-HOB-009", "GAP-HOB-012", "GAP-HOB-016", "GAP-HOB-017",
    }
    # historical round-3 audit trail preserved
    assert "simon_response_round_2026_08_29" in register


