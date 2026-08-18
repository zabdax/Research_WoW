from research.acquisition.archival_schemas import BeamMapRecord, CampaignWindowRecord


def test_beam_map_requires_primary_calibration_metadata():
    incomplete = BeamMapRecord("", "1977-08-15", 180, 0.5, 162, "", "", "")
    complete = BeamMapRecord("OSU-1", "1977-08-15", 180, 0.5, 162, "east-west", "drift scan", "archive:OSU-1")
    assert not incomplete.valid_for_confirmatory_geometry()
    assert complete.valid_for_confirmatory_geometry()


def test_campaign_window_requires_completeness_and_pointing():
    incomplete = CampaignWindowRecord("x", "", "", "", "", 1e9, 2e9, 1.0, "", "")
    complete = CampaignWindowRecord("x", "1977-01-01T00:00:00Z", "1977-01-01T01:00:00Z", "19h25m02s", "-26d57m", 1e9, 2e9, 1.0, "threshold-only", "doi:test")
    assert not incomplete.valid_for_quantitative_selection()
    assert complete.valid_for_quantitative_selection()
