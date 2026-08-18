"""Explicitly calibration-gated Big Ear response model.

The model provides conditional geometry calculations. It refuses confirmatory
use when configured only with approximate/secondary beam calibration.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from research.geometry.beam import gaussian_power_response
from research.geometry.coordinates import angular_separation_deg, parse_declination, parse_right_ascension, ra_offset_seconds


@dataclass(frozen=True)
class BeamCalibration:
    ra_fwhm_seconds: float
    dec_fwhm_deg: float
    horn_offset_seconds: float
    status: Literal["exploratory", "confirmed"]
    source: str
    locator: str
    notes: str = ""

    def __post_init__(self) -> None:
        if self.ra_fwhm_seconds <= 0 or self.dec_fwhm_deg <= 0 or self.horn_offset_seconds <= 0:
            raise ValueError("Beam calibration widths and horn offset must be positive.")


@dataclass(frozen=True)
class GeometryResult:
    angular_separation_deg: float
    ra_offset_seconds: float
    dec_offset_deg: float
    normalized_response: float
    confirmatory_eligible: bool


class BigEarGeometryModel:
    def __init__(self, calibration: BeamCalibration):
        self.calibration = calibration

    def response(self, source_ra: str, source_dec: str, pointing_ra: str, pointing_dec: str) -> GeometryResult:
        source_ra_deg, pointing_ra_deg = parse_right_ascension(source_ra), parse_right_ascension(pointing_ra)
        source_dec_deg, pointing_dec_deg = parse_declination(source_dec), parse_declination(pointing_dec)
        ra_seconds = ra_offset_seconds(pointing_ra_deg, source_ra_deg)
        dec_offset = source_dec_deg - pointing_dec_deg
        # Separable Gaussian is an explicit approximation, not a recovered beam map.
        ra_response = gaussian_power_response(ra_seconds / self.calibration.ra_fwhm_seconds)
        dec_response = gaussian_power_response(dec_offset / self.calibration.dec_fwhm_deg)
        return GeometryResult(
            angular_separation_deg=angular_separation_deg(source_ra_deg, source_dec_deg, pointing_ra_deg, pointing_dec_deg),
            ra_offset_seconds=ra_seconds,
            dec_offset_deg=dec_offset,
            normalized_response=ra_response * dec_response,
            confirmatory_eligible=self.calibration.status == "confirmed",
        )

    def require_confirmatory_calibration(self) -> None:
        if self.calibration.status != "confirmed":
            raise RuntimeError("Big Ear beam calibration is exploratory; it cannot supply confirmatory evidence.")

    def horn_nonrepeat_constraint(self, signal_duration_seconds: float) -> bool:
        """Whether a duration can be shorter than the horn separation."""
        return signal_duration_seconds < self.calibration.horn_offset_seconds
