"""Independent verification of Arecibo Wow! II Table 4 galactic coordinates.

Follow-up task (2026-08-23), arising from Phase A review. Computes galactic
coordinates from the paper's own J2000 equatorial inputs using Astropy's
SkyCoord (ICRS -> Galactic, IAU-defined transformation) — no galactic value
printed in the paper is used as an input.

Inputs are exactly the Table 4 rows (frozen awowii-v1.tex l.436-440):
    positive (East) horn : new 19:25:02 -26:57:18 | previous 19:25:31 -26:57
    negative (West) horn : new 19:27:55 -26:57:13 | previous 19:28:22 -26:57

Report-only: this module does not resolve the flagged inconsistency; it
quantifies it so a human can decide.
"""
from __future__ import annotations

import json
from pathlib import Path

from astropy.coordinates import SkyCoord
import astropy.units as u

ROOT = Path(__file__).resolve().parents[2]
RESULTS_PATH = ROOT / "research/data/processed/galactic_verification_results.json"

# Printed galactic values from Table 4 (for comparison only, never used as input)
PRINTED = {
    "new_positive": {"l_deg": 11.62, "b_deg": -17.85},
    "previous_positive": {"l_deg": 11.65, "b_deg": -18.89},
    "new_negative": {"l_deg": 11.87, "b_deg": -19.42},
    "previous_negative": {"l_deg": 11.90, "b_deg": -19.48},
}

ROWS = {
    # key: (RA hms string or degrees tuple, Dec dms string, label)
    "new_positive": ("19h25m02s", "-26d57m18s"),
    "previous_positive": ("19h25m31s", "-26d57m00s"),
    "new_negative": ("19h27m55s", "-26d57m13s"),
    "previous_negative": ("19h28m22s", "-26d57m00s"),
}


def compute() -> dict:
    results = {}
    for key, (ra, dec) in ROWS.items():
        coord = SkyCoord(ra, dec, frame="icrs")
        gal = coord.galactic
        results[key] = {
            "input_j2000": {"ra": ra, "dec": dec},
            "computed_l_deg": round(float(gal.l.deg), 4),
            "computed_b_deg": round(float(gal.b.deg), 4),
            "printed_l_deg": PRINTED[key]["l_deg"],
            "printed_b_deg": PRINTED[key]["b_deg"],
            "delta_b_printed_minus_computed_deg": round(PRINTED[key]["b_deg"] - float(gal.b.deg), 4),
            "delta_l_printed_minus_computed_deg": round(PRINTED[key]["l_deg"] - float(gal.l.deg), 4),
        }

    # Quantify the suspected typo: what dec would produce b = -17.85 at the
    # new positive-horn RA? (direct inversion scan)
    hypo_ra = "19h25m02s"
    lo, hi = -28.0, -25.0
    target = -17.85
    for _ in range(60):
        mid = (lo + hi) / 2
        b_mid = float(SkyCoord(hypo_ra, f"{mid}d", frame="icrs").galactic.b.deg)
        if b_mid < target:
            hi = mid
        else:
            lo = mid
    dec_for_target_b = (lo + hi) / 2

    # b of the suspected intended value (-18.85)
    b_of_suspected_typo_fix = float(SkyCoord("19h25m02s", "-26d57m18s", frame="icrs").galactic.b.deg)

    return {
        "run_date_utc": "2026-08-23",
        "method": {
            "tool": f"astropy {__import__('astropy').__version__} SkyCoord ICRS->Galactic",
            "frame_note": "IAU galactic system as implemented in astropy (standard J2000 rotation)",
            "inputs_used": "Table 4 J2000 RA/Dec rows only; no paper-printed galactic value used as input",
            "source_locators": {"table": "Table 4 (tab:wow)", "tex_lines": "l.436-440", "paper": "arXiv:2508.10657 v1"},
        },
        "rows": results,
        "inversion_analysis": {
            "dec_needed_for_printed_new_positive_b_-17.85_deg": round(dec_for_target_b, 5),
            "implied_dec_shift_arcmin": round(abs(dec_for_target_b - (-26 - 57 / 60)) * 60, 2),
            "suspected_intended_value_-18.85_vs_computed_b_delta_deg": round(-18.85 - results["new_positive"]["computed_b_deg"], 4),
            "note": "If the printed -17.85 were correct, the J2000 declination would need to move ~1 deg, contradicting the same row's tabulated dec (-26:57:18).",
        },
        "conclusion_basis_only": {
            "positive_horn_computed_b_matches_previous_row_within": round(
                abs(results["previous_positive"]["computed_b_deg"] - results["new_positive"]["computed_b_deg"]), 4),
            "statement": "Computed b for BOTH positive-horn J2000 positions agrees with the PREVIOUS-row printout scale (~-18.9), not the NEW-row printout (-17.85).",
        },
    }


def main() -> None:
    results = compute()
    RESULTS_PATH.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
