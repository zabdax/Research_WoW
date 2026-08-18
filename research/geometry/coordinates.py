"""Coordinate and transit utilities used by geometry-gated analyses."""
from __future__ import annotations

import math
import re


def parse_right_ascension(value: str) -> float:
    match = re.fullmatch(r"\s*(\d+(?:\.\d+)?)h(\d+(?:\.\d+)?)m(\d+(?:\.\d+)?)s\s*", value)
    if not match:
        raise ValueError(f"Invalid RA sexagesimal string: {value!r}")
    h, m, s = map(float, match.groups())
    if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
        raise ValueError(f"RA components outside range: {value!r}")
    return 15.0 * (h + m / 60.0 + s / 3600.0)


def parse_declination(value: str) -> float:
    match = re.fullmatch(r"\s*([+-])(\d+(?:\.\d+)?)d(\d+(?:\.\d+)?)m(?:(\d+(?:\.\d+)?)s)?\s*", value)
    if not match:
        raise ValueError(f"Invalid declination sexagesimal string: {value!r}")
    sign, d, m, s = match.groups()
    d, m, s = float(d), float(m), float(s or 0.0)
    if not (0 <= d <= 90 and 0 <= m < 60 and 0 <= s < 60):
        raise ValueError(f"Declination components outside range: {value!r}")
    magnitude = d + m / 60.0 + s / 3600.0
    return -magnitude if sign == "-" else magnitude


def angular_separation_deg(ra1_deg: float, dec1_deg: float, ra2_deg: float, dec2_deg: float) -> float:
    """Great-circle separation using numerically stable haversine algebra."""
    ra1, dec1, ra2, dec2 = map(math.radians, (ra1_deg, dec1_deg, ra2_deg, dec2_deg))
    a = math.sin((dec2 - dec1) / 2) ** 2 + math.cos(dec1) * math.cos(dec2) * math.sin((ra2 - ra1) / 2) ** 2
    return math.degrees(2 * math.asin(min(1.0, math.sqrt(a))))


def ra_offset_seconds(ra1_deg: float, ra2_deg: float) -> float:
    """Signed shortest RA offset in seconds of sidereal time."""
    delta_deg = (ra2_deg - ra1_deg + 180.0) % 360.0 - 180.0
    return delta_deg / 15.0 * 3600.0


def transit_time_offset_seconds(ra_offset_sidereal_seconds: float) -> float:
    """Approximate offset in transit time; RA sidereal seconds are time seconds."""
    return ra_offset_sidereal_seconds
