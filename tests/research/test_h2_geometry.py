from research.geometry.big_ear import BeamCalibration, BigEarGeometryModel
from research.models.h2_geometry import CometEphemerisRecord, intersection_result


def test_h2_requires_authoritative_ephemeris_and_confirmed_beam():
    model = BigEarGeometryModel(BeamCalibration(180.0, 0.5, 162.0, "exploratory", "test", "test"))
    comet = CometEphemerisRecord("266P", "1977-08-15", "J2000", "19h25m02s", "-26d57m", None, "secondary", "test", "test")
    result = intersection_result(model, comet, "19h25m02s", "-26d57m")
    assert result["normalized_response"] == 1.0
    assert not result["confirmatory_eligible"]
    assert result["status"] == "blocked"
