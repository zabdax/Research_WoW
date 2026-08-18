from pathlib import Path

from research.acquisition.horizons import parse_observer_ephemeris


def test_cached_horizons_response_parses_with_explicit_missing_uncertainty():
    raw = Path("research/data/raw/horizons_266p_1977_geocentric.txt")
    records = parse_observer_ephemeris(raw, "test-url", "90001240;", "500")
    assert len(records) == 25  # Horizons includes the requested stop epoch.
    assert records[0].epoch_utc == "1977-Aug-15 00:00"
    assert records[0].right_ascension == "18h32m14.64s"
    assert records[0].frame == "ICRF"
    assert records[0].uncertainty_status == "not_provided_in_response"


def test_horizons_parser_rejects_non_ephemeris_probe():
    raw = Path("research/data/raw/horizons_266p_1977_probe.txt")
    try:
        parse_observer_ephemeris(raw, "test-url", "266P", "500")
    except ValueError as error:
        assert "SOE/EOE" in str(error)
    else:
        raise AssertionError("Search-result response must not parse as an ephemeris.")
