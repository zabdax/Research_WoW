from pathlib import Path

from research.validation.source_audit import audit


def test_revised_observation_provenance_is_complete():
    path = Path("research/data/wow_observation.yaml")
    report = audit(path)
    assert report["passed"]
    assert report["records_checked"] >= 8
