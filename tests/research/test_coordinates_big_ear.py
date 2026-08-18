import pytest

from research.geometry.big_ear import BeamCalibration, BigEarGeometryModel
from research.geometry.coordinates import angular_separation_deg, parse_declination, parse_right_ascension, ra_offset_seconds


def test_sexagesimal_parsing_and_zero_separation():
    ra = parse_right_ascension("19h25m02s")
    dec = parse_declination("-26d57m")
    assert ra == pytest.approx(291.2583333333)
    assert dec == pytest.approx(-26.95)
    assert angular_separation_deg(ra, dec, ra, dec) == pytest.approx(0.0)


def test_ra_offset_is_antisymmetric():
    first, second = parse_right_ascension("19h25m02s"), parse_right_ascension("19h27m55s")
    assert ra_offset_seconds(first, second) == pytest.approx(-ra_offset_seconds(second, first))


def test_exploratory_geometry_cannot_be_confirmatory():
    model = BigEarGeometryModel(BeamCalibration(180.0, 0.5, 162.0, "exploratory", "test", "test"))
    result = model.response("19h25m02s", "-26d57m", "19h25m02s", "-26d57m")
    assert result.normalized_response == pytest.approx(1.0)
    assert not result.confirmatory_eligible
    with pytest.raises(RuntimeError):
        model.require_confirmatory_calibration()
