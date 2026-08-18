"""H2 geometry calculations with an authoritative-ephemeris gate."""
from __future__ import annotations
from dataclasses import dataclass

from research.geometry.big_ear import BigEarGeometryModel


@dataclass(frozen=True)
class CometEphemerisRecord:
    object_id: str
    epoch_utc: str
    frame: str
    right_ascension: str
    declination: str
    uncertainty_arcmin: float | None
    provenance_class: str
    source: str
    locator: str

    @property
    def authoritative(self) -> bool:
        return self.provenance_class == "authoritative"


def intersection_result(model: BigEarGeometryModel, comet: CometEphemerisRecord, wow_ra: str, wow_dec: str) -> dict[str, object]:
    geometry = model.response(comet.right_ascension, comet.declination, wow_ra, wow_dec)
    return {
        "object_id": comet.object_id,
        "angular_separation_deg": geometry.angular_separation_deg,
        "normalized_response": geometry.normalized_response,
        "confirmatory_eligible": comet.authoritative and geometry.confirmatory_eligible,
        "status": "ready_for_geometry_only" if comet.authoritative and geometry.confirmatory_eligible else "blocked",
        "blocker": "Authoritative 1977 ephemeris and confirmed Big Ear beam calibration are both required.",
    }
