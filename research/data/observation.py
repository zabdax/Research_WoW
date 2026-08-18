"""Typed observational inputs for the revised, generative analysis."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Literal


class VerificationStatus(str, Enum):
    VERIFIED = "VERIFIED"
    PARTIAL = "PARTIAL"
    UNVERIFIED = "UNVERIFIED"
    UNVERIFIED_PRIMARY = "UNVERIFIED-PRIMARY"


@dataclass(frozen=True)
class Provenance:
    source: str
    locator: str
    status: VerificationStatus
    notes: str = ""


@dataclass(frozen=True)
class CensoredMeasurement:
    """A measurement, interval, or one-sided observational constraint in SI units."""

    value: float
    unit: str
    kind: Literal["point", "lower_bound", "upper_bound", "interval"] = "point"
    uncertainty: float | None = None
    provenance: Provenance | None = None


@dataclass(frozen=True)
class SkyCandidate:
    right_ascension: str
    declination: str
    epoch: str
    ra_uncertainty_seconds: float | None
    dec_uncertainty_arcmin: float | None
    provenance: Provenance


@dataclass(frozen=True)
class FollowUpObservation:
    identifier: str
    telescope: str
    exposure_seconds: float | None
    frequency_low_hz: float | None
    frequency_high_hz: float | None
    channel_width_hz: float | None
    flux_limit_jy: float | None
    field_of_view_deg: float | None
    pointing_ra: str | None
    pointing_dec: str | None
    cadence_description: str
    provenance: Provenance


@dataclass(frozen=True)
class WowObservation:
    event_date: str
    frequency: CensoredMeasurement
    bandwidth: CensoredMeasurement
    flux_density: CensoredMeasurement
    snr: CensoredMeasurement
    beam_crossing_duration: CensoredMeasurement
    horn_turnon_window: CensoredMeasurement
    sky_candidates: tuple[SkyCandidate, ...]
    followup: tuple[FollowUpObservation, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class ObservationBundle:
    event: WowObservation
    schema_version: str = "0.1.0"
    interpretation: str = (
        "Measurement constraints only. Physical mechanism and event-rate "
        "assumptions belong to hypothesis models."
    )
