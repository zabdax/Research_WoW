"""Validators that prevent incomplete archival records from entering evidence models."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class BeamMapRecord:
    archival_id: str
    instrument_date: str
    ra_fwhm_seconds: float
    dec_fwhm_deg: float
    horn_offset_seconds: float
    horn_orientation: str
    calibration_method: str
    source_locator: str

    def valid_for_confirmatory_geometry(self) -> bool:
        return bool(self.archival_id and self.instrument_date and self.horn_orientation and self.calibration_method and self.source_locator) and self.ra_fwhm_seconds > 0 and self.dec_fwhm_deg > 0 and self.horn_offset_seconds > 0


@dataclass(frozen=True)
class CampaignWindowRecord:
    campaign_id: str
    start_utc: str
    end_utc: str
    pointing_ra: str
    pointing_dec: str
    frequency_low_hz: float
    frequency_high_hz: float
    flux_limit_jy: float
    completeness_description: str
    source_locator: str

    def valid_for_quantitative_selection(self) -> bool:
        return bool(self.campaign_id and self.start_utc and self.end_utc and self.pointing_ra and self.pointing_dec and self.completeness_description and self.source_locator) and self.frequency_low_hz > 0 and self.frequency_high_hz >= self.frequency_low_hz and self.flux_limit_jy > 0


def validate_mapping(record: Mapping[str, object], required: set[str]) -> list[str]:
    return sorted(key for key in required if record.get(key) in (None, ""))
