from pathlib import Path

from research.models.h2_horizons_sensitivity import geocentric_offset_report


def test_h2_horizons_sensitivity_is_explicitly_non_confirmatory():
    report = geocentric_offset_report()
    assert not report["confirmatory_eligible"]
    assert report["offsets_deg"]["candidate_a"] > 10
    assert "must not be reported" in report["interpretation"]


def test_second_h2_ephemeris_is_separately_gated():
    report = geocentric_offset_report(Path("research/data/processed/horizons_335p_1977_geocentric.json"))
    assert not report["confirmatory_eligible"]
    assert report["offsets_deg"]["candidate_a"] > 10
