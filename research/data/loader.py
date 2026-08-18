"""Load versioned observation records without converting bounds into point estimates."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from research.data.observation import (
    CensoredMeasurement,
    FollowUpObservation,
    ObservationBundle,
    Provenance,
    SkyCandidate,
    VerificationStatus,
    WowObservation,
)


def _provenance(value: dict[str, Any]) -> Provenance:
    return Provenance(
        source=value["source"],
        locator=value["locator"],
        status=VerificationStatus(value["status"]),
        notes=value.get("notes", ""),
    )


def _measurement(value: dict[str, Any]) -> CensoredMeasurement:
    return CensoredMeasurement(
        value=float(value["value"]),
        unit=value["unit"],
        kind=value.get("kind", "point"),
        uncertainty=value.get("uncertainty"),
        provenance=_provenance(value),
    )


def load_wow_observation(path: str | Path | None = None) -> ObservationBundle:
    source_path = Path(path) if path else Path(__file__).with_name("wow_observation.yaml")
    raw = yaml.safe_load(source_path.read_text(encoding="utf-8"))
    event = raw["event"]
    candidates = tuple(
        SkyCandidate(
            right_ascension=item["right_ascension"],
            declination=item["declination"],
            epoch=item["epoch"],
            ra_uncertainty_seconds=item.get("ra_uncertainty_seconds"),
            dec_uncertainty_arcmin=item.get("dec_uncertainty_arcmin"),
            provenance=_provenance(item),
        )
        for item in event["sky_candidates"]
    )
    followup = tuple(
        FollowUpObservation(
            identifier=item["identifier"],
            telescope=item["telescope"],
            exposure_seconds=item.get("exposure_seconds"),
            frequency_low_hz=item.get("frequency_low_hz"),
            frequency_high_hz=item.get("frequency_high_hz"),
            channel_width_hz=item.get("channel_width_hz"),
            flux_limit_jy=item.get("flux_limit_jy"),
            field_of_view_deg=item.get("field_of_view_deg"),
            pointing_ra=item.get("pointing_ra"),
            pointing_dec=item.get("pointing_dec"),
            cadence_description=item["cadence_description"],
            provenance=_provenance(item),
        )
        for item in raw.get("followup", [])
    )
    return ObservationBundle(
        schema_version=raw["schema_version"],
        event=WowObservation(
            event_date=event["event_date"],
            frequency=_measurement(event["frequency"]),
            bandwidth=_measurement(event["bandwidth"]),
            flux_density=_measurement(event["flux_density"]),
            snr=_measurement(event["snr"]),
            beam_crossing_duration=_measurement(event["beam_crossing_duration"]),
            horn_turnon_window=_measurement(event["horn_turnon_window"]),
            sky_candidates=candidates,
            followup=followup,
        ),
    )
