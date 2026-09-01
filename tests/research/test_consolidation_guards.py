"""Consolidation-phase guard tests (POST-G&E/POST-SIMON directive, Part 11).

Enforces the evidence-status distinctions created by the consolidation
documents so they cannot silently disappear:

- five-way comparison stays disabled; no inference quantities;
- Mendez evidence vector hash-consistent;
- the 1998/99 non-detection stays a PUBLISHED historical outcome and is
  never auto-converted into a likelihood;
- Simon's "~50% accuracy" stays qualitative (no sigma=50% encoding);
- 2010 intent stays unresolved (donor speculation class intact);
- 2013/14 calibration stays provisional/donor-limited;
- historical (1998/99) and modern (2010-14) evidence stay era-separated;
- the consolidation documents exist with their guardian distinctions intact.
"""

import hashlib
import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
DOCS = REPO / "docs" / "acquisition"
DATA = REPO / "research" / "data"

BASELINE = DOCS / "HOBART_1998_99_EVIDENCE_BASELINE.md"
GAPS_AFTER = DOCS / "HOBART_REMAINING_GAPS_AFTER_GE2002_SIMON.md"
DNA = DOCS / "bob_gray_do_not_ask_again.md"
AUDIT = DOCS / "HOBART_2010_2013_14_DATA_AUDIT.md"
SUMMARY = DOCS / "bob_gray_evidence_summary.md"
EMAIL = DOCS / "bob_gray_email_draft.md"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_consolidation_documents_exist():
    for p in (BASELINE, GAPS_AFTER, DNA, AUDIT, SUMMARY, EMAIL):
        assert p.exists(), f"missing consolidation artifact: {p.name}"


def test_baseline_guardian_distinctions_intact():
    text = BASELINE.read_text(encoding="utf-8")
    assert "published non-detection != reconstructed selection function" in text
    assert "raw archival data  != independently reproduced historical search" in text or \
        "raw archival data != independently reproduced historical search" in text
    assert "PUBLISHED_RESULT_WITHOUT_SURVIVING_CANDIDATE_LEVEL_DATA" in text
    assert "NOT_STATED" in text and "UNKNOWN" in text


def test_baseline_15_questions_answered():
    text = BASELINE.read_text(encoding="utf-8")
    for q in range(1, 16):
        assert re.search(rf"## Q{q} —", text), f"baseline missing Q{q}"


def test_do_not_ask_record_covers_both_sources():
    text = DNA.read_text(encoding="utf-8")
    assert "Already answered by Simon" in text
    assert "Already answered by Gray & Ellingsen (2002)" in text
    assert "executed implementation" in text  # the one allowed nuance


def test_later_campaign_audit_era_separation():
    text = AUDIT.read_text(encoding="utf-8")
    assert "GE2002 published outcome covers **only** the 1998/99 era" in text or \
        "only** the 1998/99 era" in text
    assert "NOT σ=50%" in text or "NOT a Gaussian" in text or "NOT σ" in text


def test_email_draft_not_send_marker():
    text = EMAIL.read_text(encoding="utf-8")
    assert "DO NOT SEND" in text
    assert "has NOT been sent" in text


def test_gap_register_v13_invariants():
    register = yaml.safe_load((DATA / "ellingsen_gap_register.yaml").read_text(encoding="utf-8"))
    assert register["register_version"] == 1.3
    g = register["gaps"]
    # 2010 intent remains unresolved donor speculation
    assert g["GAP-HOB-004"]["round3_amendment"]["donor_statement_class"] == "UNVERIFIED_DONOR_SPECULATION"
    # 2013/14 calibration stays provisional; ~50% never encoded as sigma
    assert g["GAP-HOB-010"]["status"] == "PROVISIONAL_DONOR_LIMITED"
    assert "sigma = 50%" in g["GAP-HOB-010"]["round3_amendment"]["forbidden_encoding"]
    raw = (DATA / "ellingsen_gap_register.yaml").read_text(encoding="utf-8")
    assert "sigma: 0.5" not in raw and "sigma_2013: 0.5" not in raw
    # era-split statuses persist
    for gap_id in ("GAP-HOB-005", "GAP-HOB-009"):
        assert g[gap_id]["status"].startswith("RESOLVED_LOCAL_1998_99")
    # historical audit trails preserved
    assert "simon_response_round_2026_08_29" in register
    assert "ge2002_extraction_round" in register


def test_published_outcome_stays_historical():
    outcome = yaml.safe_load((DATA / "ge2002_search_outcome.yaml").read_text(encoding="utf-8"))
    assert outcome["published_outcome"]["verdict"] == "PUBLISHED_NON_DETECTION"
    assert outcome["selection_function_status"]["can_reconstruct_full_selection_function"] == "NO"


def test_five_way_gate_and_evidence_vector_unchanged():
    cfg = yaml.safe_load((REPO / "configs" / "research_status.yaml").read_text(encoding="utf-8"))
    assert cfg["confirmatory_comparison_enabled"] is False
    manifest = yaml.safe_load((DATA / "mendez_evidence_freeze_manifest.yaml").read_text(encoding="utf-8"))
    pinned = manifest["frozen_files"]["mendez_evidence_vector"]["sha256"]
    assert _sha256(DATA / "mendez_evidence_vector.yaml") == pinned


def test_no_inference_quantities_in_consolidation_docs():
    for p in (BASELINE, GAPS_AFTER, AUDIT, SUMMARY):
        text = p.read_text(encoding="utf-8").lower()
        for forbidden in ("bayes factor:", "posterior odds:", "p(data|h5)",
                          "p(no detection|h5)", "detection efficiency ="):
            assert forbidden not in text, f"forbidden quantity in {p.name}: {forbidden}"
