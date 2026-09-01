"""Directive 2026-08-29 section 29 tests.

Guards for the Simon-Ellingsen donor-response freeze and the 1998/99 MPSLPP
software archaeology:
  1.  Simon response record exists
  2.  donor-response provenance vocabulary is valid
  3.  archive completeness is not mislabeled as historical completeness
  4.  donor speculation cannot become observational fact
  5.  2013/14 ~50% calibration statement is not converted to a Gaussian sigma
  6.  five-way comparison remains disabled
  7.  no H5 likelihood/posterior artifact is emitted
  8.  Arecibo evidence vector remains unchanged
  9.  original Fortran/documentation hashes remain fixed
  10. missing dependencies are explicitly represented
  11. no inference quantities are produced (key-level scan of new artifacts)

No existing test is modified or weakened.
"""

import hashlib
import json
import re
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "research" / "data"
CONFIGS = REPO / "configs"
SRC = REPO / "research" / "sources" / "ellingsen_hobart"
DONOR_FOLDER = REPO / "reresearchdatarequestarchivalhobartfollowupobserv"

SIMON_YAML = DATA / "ellingsen_simon_response.yaml"
GAP_REGISTER = DATA / "ellingsen_gap_register.yaml"
FORT_INV = DATA / "ellingsen_fortran_inventory.yaml"
DEP_MAP = SRC / "analysis" / "fortran_dependency_map.json"
FREEZE_MANIFEST = DATA / "mendez_evidence_freeze_manifest.yaml"
EVIDENCE_VECTOR = DATA / "mendez_evidence_vector.yaml"
STATUS_CONFIG = CONFIGS / "research_status.yaml"
SUMS = SRC / "hashes" / "SIMON_SOFTWARE_SHA256SUMS.txt"

ALLOWED_EVIDENCE_CLASSES = {"DONOR_TESTIMONY", "DONOR_SPECULATION",
                            "DOCUMENTARY", "DONOR_TESTIMONY + DOCUMENTARY (supplied artifacts)"}
FORBIDDEN_KEY_RE = re.compile(
    r"(?i)likelihood|posterior|bayes|detection_efficiency|non_detection|"
    r"shared_rate|odds|evidence_vector_update"
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _walk_keys(node):
    if isinstance(node, dict):
        for k, v in node.items():
            yield str(k)
            yield from _walk_keys(v)
    elif isinstance(node, list):
        for item in node:
            yield from _walk_keys(item)


@pytest.fixture(scope="module")
def simon():
    with open(SIMON_YAML, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


@pytest.fixture(scope="module")
def gaps():
    with open(GAP_REGISTER, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


@pytest.fixture(scope="module")
def dep_map():
    return json.loads(DEP_MAP.read_text(encoding="utf-8"))

# --- 1. Simon response record exists ----------------------------------------


def test_simon_response_exists_and_parses(simon):
    assert simon["freeze_version"] == 1.0
    assert simon["donor"].startswith("Simon Ellingsen")
    assert len(simon["answers"]) == 9
    assert simon["original_email_metadata"]["locally_archived"] is False


# --- 2. Provenance vocabulary is valid ---------------------------------------


def test_donor_vocabulary_valid(simon):
    for qid, ans in simon["answers"].items():
        assert ans["evidence_class"] in ALLOWED_EVIDENCE_CLASSES, qid
        assert re.fullmatch(r"[A-Z0-9_]+", ans["scientific_status"]), qid
        assert ans["verbatim_answer"].strip(), qid
        assert ans["affected_gaps"], qid


# --- 3. Completeness is not mislabeled ---------------------------------------


def test_completeness_not_mislabeled(simon):
    q1 = simon["answers"]["Q1_archive_completeness"]
    assert q1["scientific_status"] == "DONOR_SIDE_SURVIVING_ARCHIVE_COMPLETENESS_RESOLVED"
    assert "NOT" in q1["interpretation"]
    assert "complete historical" in q1["interpretation"].lower()
    rule = simon["completeness_rule"]
    assert rule["archive_completeness_label"] == "complete surviving donor-held material"
    assert rule["forbidden_label"] == "complete historical Hobart archive"


# --- 4. Donor speculation cannot become observational fact --------------------


def test_speculation_not_fact(simon, gaps):
    q4 = simon["answers"]["Q4_2010_pointing"]
    assert q4["evidence_class"] == "DONOR_SPECULATION"
    assert q4["scientific_status"] == "UNVERIFIED_DONOR_SPECULATION"
    assert "MUST NOT" in q4["interpretation"]
    r3 = gaps["gaps"]["GAP-HOB-004"]["round3_amendment"]
    assert r3["donor_statement_class"] == "UNVERIFIED_DONOR_SPECULATION"


# --- 5. ~50% calibration statement is not a Gaussian sigma --------------------


def test_calibration_50pct_not_sigma(simon, gaps):
    q7 = simon["answers"]["Q7_2013_14_calibration"]
    assert q7["scientific_status"] == "ABSOLUTE_CALIBRATION_PROVISIONAL_DONOR_LIMITED"
    assert "NOT a" in q7["interpretation"]
    for gap_id in ("GAP-HOB-010", "GAP-HOB-011"):
        r3 = gaps["gaps"][gap_id]["round3_amendment"]
        assert "sigma = 50%" in r3["forbidden_encoding"]
    assert gaps["gaps"]["GAP-HOB-010"]["status"] == "PROVISIONAL_DONOR_LIMITED"

# --- 6. Five-way comparison remains disabled ----------------------------------


def test_five_way_gate_stays_closed():
    cfg = yaml.safe_load(STATUS_CONFIG.read_text(encoding="utf-8"))
    assert cfg["confirmatory_comparison_enabled"] is False
    assert cfg["analysis_stage"] == "reconstruction"


# --- 7./11. No inference quantities emitted (key-level scan) -------------------


@pytest.mark.parametrize("artifact", ["dep_map", "fortran_inventory", "simon"])
def test_no_inference_quantities_emitted(artifact, dep_map, simon):
    if artifact == "dep_map":
        payload = dep_map
    elif artifact == "simon":
        payload = simon
    else:
        payload = yaml.safe_load(FORT_INV.read_text(encoding="utf-8"))
    forbidden = [k for k in _walk_keys(payload) if FORBIDDEN_KEY_RE.search(k)]
    assert forbidden == [], f"inference-like keys leaked into {artifact}: {forbidden}"


# --- 8. Arecibo evidence vector remains unchanged ------------------------------


def test_arecibo_evidence_vector_unchanged():
    manifest = yaml.safe_load(FREEZE_MANIFEST.read_text(encoding="utf-8"))
    pinned = manifest["frozen_files"]["mendez_evidence_vector"]["sha256"]
    assert manifest["frozen_files"]["mendez_evidence_vector"]["freeze_status"] == "FROZEN"
    assert _sha256(EVIDENCE_VECTOR) == pinned, "FROZEN Arecibo evidence vector was modified!"


# --- 9. Fortran/documentation hashes remain fixed ------------------------------


def _expected_sums():
    expected = {}
    for line in SUMS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest, rel = line.split(maxsplit=1)
            expected[rel.strip()] = digest.lower()
    return expected


def test_frozen_software_hashes_fixed():
    expected = _expected_sums()
    assert set(expected) == {"software/mpslpp.f", "documentation/mpslpp.tex"}
    for rel, digest in expected.items():
        path = SRC / rel
        assert path.exists(), f"frozen copy missing: {rel}"
        assert _sha256(path) == digest, f"frozen copy hash drift: {rel}"
        donor_copy = DONOR_FOLDER / Path(rel).name
        if donor_copy.exists():  # originals stay byte-for-byte unchanged
            assert _sha256(donor_copy) == digest, f"donor original changed: {rel}"

# --- 10. Missing dependencies are explicitly represented -----------------------


def test_missing_dependencies_explicit(dep_map):
    counts = dep_map["fortran"]["dependency_counts"]
    assert counts["FOUND"] == 0
    assert counts["FOUND_PARTIAL"] == 0
    assert counts["REFERENCED_BUT_MISSING"] == 73
    deps = dep_map["fortran"]["dependencies"]
    for inc in ("include:mpslpp.inc", "include:headkey.inc",
                "include:histkey.inc", "include:mpslpp.def"):
        assert deps[inc]["classification"] == "REFERENCED_BUT_MISSING"
    for kernel in ("vanvleck", "dofft", "hanning", "readfit", "writefit"):
        assert deps[kernel]["classification"] == "REFERENCED_BUT_MISSING"


def test_mpslpp_identity_supports_data_interpretation(dep_map):
    f = dep_map["fortran"]
    assert f["version"] == "1.8"
    assert f["parameters_extracted"]["maxlag"] == "1024"
    names = {u["name"] for u in f["program_units"]}
    assert names == {"mpslpp", "extrtn"}
    assert dep_map["documentation"]["key_statements"]["data_form_in_correlator_files"] == \
        "autocorrelation functions"


# --- Gap-register integrity for this round -------------------------------------


def test_gap_register_round3_audit_complete(gaps):
    audit = gaps["simon_response_round_2026_08_29"]["changes"]
    touched = {c["gap"] for c in audit}
    assert touched == {
        "GAP-HOB-001", "GAP-HOB-002", "GAP-HOB-003", "GAP-HOB-004",
        "GAP-HOB-005", "GAP-HOB-006", "GAP-HOB-007", "GAP-HOB-008",
        "GAP-HOB-009", "GAP-HOB-010", "GAP-HOB-011", "GAP-HOB-012",
        "GAP-HOB-014",
    }
    assert gaps["register_version"] == 1.3
    # Historical note (v1.3): the round-3 closures for the search-layer gaps
    # were superseded for the 1998/99 era by the GE2002 paper extraction
    # (statuses became era-split RESOLVED_LOCAL_1998_99__OPEN_2010_2014); the
    # round-3 audit block below is preserved unchanged.
    assert "simon_response_round_2026_08_29" in gaps
    audit = gaps["simon_response_round_2026_08_29"]["changes"]
    assert {c["gap"] for c in audit} >= {
        "GAP-HOB-005", "GAP-HOB-006", "GAP-HOB-007", "GAP-HOB-008", "GAP-HOB-009",
    }


def test_no_h5_quantities_in_gap_register(gaps):
    text = GAP_REGISTER.read_text(encoding="utf-8").lower()
    for forbidden in ("bayes factor:", "posterior odds:", "p(data|h5)",
                      "detection efficiency =", "p(no detection|h5)"):
        assert forbidden not in text, f"forbidden inference quantity: {forbidden}"



