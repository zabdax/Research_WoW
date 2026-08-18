from research.simulation.h5_assets import asset_report, parse_fortran_days


def test_upstream_fortran_dates_parse_exactly():
    days = parse_fortran_days()
    assert len(days) == 90
    assert days[0] == 0.5
    assert days[-1] == 2672.5


def test_upstream_assets_have_traceable_grid_metadata():
    report = asset_report()
    assert len(report["fortran_sha256"]) == 64
    assert report["grid"]["rows"] == 25600
    assert report["grid"]["rows"] != 150 * 160  # Bundled asset differs from declared source loops.
    assert report["status"].startswith("assets_parsed")
