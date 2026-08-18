"""Campaign-specific threshold selection functions.

They encode explicitly stated threshold constraints only. They are not full
completeness surfaces and must not be treated as a physical event-rate model.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class ThresholdCampaign:
    identifier: str
    flux_limit_jy: float | None
    frequency_low_hz: float | None
    frequency_high_hz: float | None
    channel_width_hz: float | None
    fwhm_deg: float | None
    exposure_seconds: float | None
    cadence_status: str
    selection_status: str


def gaussian_beam_attenuation(offset_deg: float, fwhm_deg: float) -> float:
    if fwhm_deg <= 0:
        raise ValueError("FWHM must be positive.")
    return math.exp(-4 * math.log(2) * (offset_deg / fwhm_deg) ** 2)


def threshold_detection_efficiency(
    campaign: ThresholdCampaign,
    flux_jy: float,
    frequency_hz: float,
    offset_deg: float = 0.0,
) -> float | None:
    """Return 0/1 for documented threshold detection, or None if unavailable."""
    if flux_jy < 0:
        raise ValueError("Flux must be non-negative.")
    if campaign.flux_limit_jy is None or campaign.fwhm_deg is None:
        return None
    if campaign.frequency_low_hz is not None and frequency_hz < campaign.frequency_low_hz:
        return 0.0
    if campaign.frequency_high_hz is not None and frequency_hz > campaign.frequency_high_hz:
        return 0.0
    attenuated_flux = flux_jy * gaussian_beam_attenuation(offset_deg, campaign.fwhm_deg)
    return float(attenuated_flux >= campaign.flux_limit_jy)


def no_detection_probability(detection_efficiencies: list[float]) -> float:
    """Conditional probability given independent supplied event opportunities."""
    if any(not 0 <= p <= 1 for p in detection_efficiencies):
        raise ValueError("Detection efficiencies must lie in [0, 1].")
    return math.prod(1.0 - p for p in detection_efficiencies)
