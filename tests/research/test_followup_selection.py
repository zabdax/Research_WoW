import pytest

from research.followup.selection import ThresholdCampaign, no_detection_probability, threshold_detection_efficiency


CAMPAIGN = ThresholdCampaign("test", 10.0, 1e9, 2e9, 1e3, 1.0, 3600.0, "known", "threshold-only")


def test_threshold_efficiency_tracks_flux_frequency_and_offset():
    assert threshold_detection_efficiency(CAMPAIGN, 11.0, 1.42e9) == 1.0
    assert threshold_detection_efficiency(CAMPAIGN, 9.0, 1.42e9) == 0.0
    assert threshold_detection_efficiency(CAMPAIGN, 100.0, 2.5e9) == 0.0
    assert threshold_detection_efficiency(CAMPAIGN, 11.0, 1.42e9, offset_deg=1.0) == 0.0


def test_no_detection_is_conditional_product():
    assert no_detection_probability([0.5, 0.5]) == pytest.approx(0.25)
