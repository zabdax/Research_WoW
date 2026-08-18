"""Report geocentric comet-to-Wow offsets without overstating them as evidence."""
from __future__ import annotations

import json
from pathlib import Path

from research.geometry.coordinates import angular_separation_deg, parse_declination, parse_right_ascension

ROOT = Path(__file__).resolve().parents[2]


def geocentric_offset_report(path: Path | None = None) -> dict[str, object]:
    source = (path or ROOT / "research" / "data" / "processed" / "horizons_266p_1977_geocentric.json").resolve()
    payload = json.loads(source.read_text(encoding="utf-8"))
    record = payload["records"][0]
    candidates = {
        "candidate_a": ("19h25m02s", "-26d57m"),
        "candidate_b": ("19h27m55s", "-26d57m"),
    }
    offsets = {
        name: angular_separation_deg(
            parse_right_ascension(record["right_ascension"]), parse_declination(record["declination"]),
            parse_right_ascension(ra), parse_declination(dec),
        )
        for name, (ra, dec) in candidates.items()
    }
    return {
        "input": str(source.relative_to(ROOT)),
        "object_solution": record["solution_command"],
        "epoch_utc": record["epoch_utc"],
        "frame": record["frame"],
        "observer_center": record["observer_center"],
        "offsets_deg": offsets,
        "interpretation": (
            "Geocentric positional sensitivity result only. It has no ephemeris covariance, "
            "does not use the Big Ear topocentric location or confirmed beam, and supplies "
            "no cometary emission/flux likelihood. It must not be reported as P(D|H2)."
        ),
        "confirmatory_eligible": False,
    }
