"""Phase C reproduction of Arecibo Wow! II (arXiv:2508.10657 v1) quantities.

Authorized scope (Phase A authorization, 2026-08-23):
  1. Frequency chain  — GENUINE independent verification (public equations +
     constants + frozen Ohio-SETI data).
  2. Flux arithmetic  — ARITHMETIC_REPRODUCTION_ONLY: the underlying noise-tube
     constants (9.4 Jy, 8.0 +/- 1.8) are paper-stated, not independently
     data-derived. A match confirms internal consistency of the paper's math,
     NOT the constants themselves.

Not attempted here (per authorization): squint/position corrections (private
strip chart), velocity transforms, beam fits.

Also runs one internal-consistency check (report-only, not a reproduction
target): Table 4 galactic coordinates vs its own previous-values column.
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PAPER_TEX = ROOT / "research/sources/mendez_arecibo/extracted/awow2_2508.10657v1_eprint/awowii-v1.tex"
OHIO_CSV = ROOT / "research/sources/mendez_arecibo/repositories/Ohio-SETI/oseti_19770815_220410.csv"
RESULTS_PATH = ROOT / "research/data/processed/mendez_reproduction_results.json"

# Paper-stated constants (frozen v1 TeX locators in parentheses)
F_2LO_PEAK = 120.185          # §7 l.322 — also data-verified below
F_2LOC_PRE = 120.1            # §7 l.322 (before 1977-12-13)
HI_REF_MHZ = 1420.4056        # §7 equation l.318
CHANNEL_MHZ = 0.010           # §7 equation l.319
WOW_CHANNEL = 2               # §7 l.322
PAPER_FC = 1420.491           # §7 l.322 (MHz)
PAPER_FREQ = 1420.726         # Table 4 l.424 (MHz)
PAPER_FREQ_UNC = 0.005        # half the 10 kHz channel (§7 l.322)

S_NTUBE_JY = 9.4              # §6 l.267
SNR_NTUBE = 8.0               # §6 l.267
SNR_NTUBE_UNC = 1.8           # §6 l.267
N_CHANNELS = 50               # §6 l.271
PAPER_SIGMA_CNT = (1.2, 0.3)  # §6 l.267
PAPER_SIGMA_CHANNEL = (8.5, 2.1)  # §6 l.271
SNR_WOW = 30.1                # §6 l.277 / fig:wowfit
SNR_WOW_UNC = 0.4
PAPER_FLUX_BOUND = 256.0      # Table 4 l.430 (>= 256)
PAPER_FLUX_UNC = 63.0

# Table 4 galactic rows (l.439-440) for the internal-consistency check
TABLE4_GALACTIC = {
    "previous_positive": (11.65, -18.89),
    "new_positive": (11.62, -17.85),
    "previous_negative": (11.90, -19.48),
    "new_negative": (11.87, -19.42),
}


def reproduce_frequency_chain() -> dict:
    """Recompute f_c and f_n from the paper's equations (§7 l.316-322)."""
    f_c = (F_2LO_PEAK - F_2LOC_PRE) + HI_REF_MHZ
    f_n = f_c + (25.5 - WOW_CHANNEL) * CHANNEL_MHZ
    return {
        "mode": "GENUINE_INDEPENDENT_VERIFICATION",
        "inputs": {
            "f_2LO_peak_mhz": F_2LO_PEAK,
            "f_2LOc_pre_19771213_mhz": F_2LOC_PRE,
            "HI_reference_mhz": HI_REF_MHZ,
            "channel_mhz": CHANNEL_MHZ,
            "channel_number": WOW_CHANNEL,
            "sources": "paper equations + frozen Ohio-SETI CSV 2LO column",
        },
        "our": {"f_c_mhz": round(f_c, 4), "f_channel2_mhz": round(f_n, 4), "uncertainty_mhz": PAPER_FREQ_UNC},
        "published": {"f_c_mhz": PAPER_FC, "f_channel2_mhz": PAPER_FREQ, "uncertainty_mhz": PAPER_FREQ_UNC},
        "absolute_difference": {"f_c_mhz": round(abs(f_c - PAPER_FC), 6), "f_channel2_mhz": round(abs(f_n - PAPER_FREQ), 6)},
        "relative_difference": {"f_channel2_mhz": round(abs(f_n - PAPER_FREQ) / PAPER_FREQ, 8)},
        "expected_tolerance": "rounding at the printed precision (1e-3 MHz)",
        "status": None,  # set by caller after comparison
    }


def verify_2lo_in_frozen_data() -> dict:
    """Data-level check: locate the Wow channel-2 sequence in the frozen
    Ohio-SETI CSV and read the 2nd-LO value at the peak rows."""
    with OHIO_CSV.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))
    data = [r + [""] * (56 - len(r)) for r in rows[1:]]
    sequence = []
    for i, row in enumerate(data, start=1):
        ch2 = (row[1] or " ").strip()
        if ch2:
            sequence.append(
                {
                    "row": i,
                    "channel_2_char": ch2,
                    "second_lo_mhz": float(row[52].strip()),
                    "est": row[55].strip(),
                }
            )
    wow_rows = [s for s in sequence if s["row"] in range(58, 64)]
    chars = "".join(s["channel_2_char"] for s in wow_rows)
    # Paper claim (l.322): 2nd LO = 120.185 MHz "at the time of the central
    # peak" — i.e. the U row. Adjacent rows differ by 0.001 MHz steps (GSR
    # tracking drift), which is expected and is NOT part of the claim.
    u_row = next(s for s in wow_rows if s["channel_2_char"] == "U")
    peak_2lo_values = {s["channel_2_char"]: s["second_lo_mhz"] for s in wow_rows if s["channel_2_char"] in "6EQUJ5"}
    return {
        "mode": "DATA_LEVEL_VERIFICATION",
        "source": {"repository": "planetaryhablab/Ohio-SETI", "commit": "28624a1eaf955ced940db347684cee61c8e4fd61",
                   "file": "oseti_19770815_220410.csv"},
        "found_sequence_rows_58_63": chars,
        "expected_sequence": "6EQUJ5",
        "sequence_match": chars == "6EQUJ5",
        "second_lo_by_sequence_char_mhz": peak_2lo_values,
        "second_lo_at_central_peak_U_row_mhz": u_row["second_lo_mhz"],
        "paper_constant_f2lo_mhz": F_2LO_PEAK,
        "match": abs(u_row["second_lo_mhz"] - F_2LO_PEAK) < 1e-9,
        "note": "Adjacent rows step by 0.001 MHz (GSR tracking drift); the paper's constant refers to the central peak (U row) specifically.",
        "peak_sample_est": "22 16 10 (U row) vs paper fit time 22:16:06 — consistent within 12 s sampling",
    }


def reproduce_flux_arithmetic() -> dict:
    """Arithmetic reproduction of the §6 chain (l.266-276), plus the unrounded
    propagation that exposes the paper's rounding policy."""
    sigma_cnt = S_NTUBE_JY / SNR_NTUBE
    sigma_cnt_unc = sigma_cnt * (SNR_NTUBE_UNC / SNR_NTUBE)
    sigma_channel_paper = PAPER_SIGMA_CNT[0] * math.sqrt(N_CHANNELS)      # paper path uses rounded 1.2
    sigma_channel_paper_unc = PAPER_SIGMA_CNT[1] * math.sqrt(N_CHANNELS)
    sigma_channel_unrounded = sigma_cnt * math.sqrt(N_CHANNELS)
    sigma_channel_unrounded_unc = sigma_cnt_unc * math.sqrt(N_CHANNELS)

    flux_paper_path = SNR_WOW * sigma_channel_paper                        # 30.1 x 8.5
    flux_unrounded = SNR_WOW * sigma_channel_unrounded

    def rel(args):
        return math.sqrt(sum((u / v) ** 2 for u, v in args))

    flux_unc_paper_path = flux_paper_path * rel([(SNR_WOW_UNC, SNR_WOW), (sigma_channel_paper_unc, sigma_channel_paper)])
    flux_unc_unrounded = flux_unrounded * rel([(SNR_WOW_UNC, SNR_WOW), (sigma_channel_unrounded_unc, sigma_channel_unrounded)])

    return {
        "mode": "ARITHMETIC_REPRODUCTION_ONLY",
        "caveat": "Underlying constants (9.4 Jy, 8.0+/-1.8) are PAPER-STATED, not independently data-derived; agreement confirms the paper's internal arithmetic consistency only.",
        "chain_paper_as_printed": {
            "sigma_cnt": f"{PAPER_SIGMA_CNT[0]} +/- {PAPER_SIGMA_CNT[1]} Jy (paper l.267)",
            "sigma_channel": f"{PAPER_SIGMA_CHANNEL[0]} +/- {PAPER_SIGMA_CHANNEL[1]} Jy (paper l.271)",
            "flux_bound": f">= {PAPER_FLUX_BOUND} +/- {PAPER_FLUX_UNC} Jy (Table 4)",
        },
        "our_reproduction_of_paper_path": {
            "sigma_channel_from_1.2": round(sigma_channel_paper, 3),
            "flux_bound": round(flux_paper_path, 2),
            "flux_uncertainty": round(flux_unc_paper_path, 1),
            "absolute_difference_vs_published": round(abs(flux_paper_path - PAPER_FLUX_BOUND), 2),
            "relative_difference_vs_published": round(abs(flux_paper_path - PAPER_FLUX_BOUND) / PAPER_FLUX_BOUND, 5),
            "status": "MATCH within printed rounding",
        },
        "unrounded_propagation_finding": {
            "sigma_cnt_unrounded": round(sigma_cnt, 4),
            "sigma_channel_unrounded": round(sigma_channel_unrounded, 3),
            "flux_bound_unrounded": round(flux_unrounded, 1),
            "flux_unc_unrounded": round(flux_unc_unrounded, 1),
            "finding": "Propagating UNROUNDED intermediates (9.4/8.0 = 1.175, x sqrt(50) = 8.31) gives >= 250.1 +/- 56 Jy, i.e. -2.3% vs the published 256: the published value embeds the upward rounding of sigma_cnt 1.175 -> 1.2. This is a rounding-policy artifact, NOT an arithmetic error. Documented, not tuned. (Observation only: the abstract's 'exceeding 250 Jy' wording coincides with the unrounded value; abstract values remain excluded from the evidence vector.)",
        },
        "expected_tolerance": "exact arithmetic modulo printed rounding",
    }


def galactic_consistency_check() -> dict:
    """Report-only check (not an authorized reproduction target): Table 4's
    new-vs-previous galactic rows. The positive-horn b jumps +1.04 deg while
    the J2000 position moved only ~29 arcsec in RA — internally inconsistent."""
    d_b_pos = TABLE4_GALACTIC["new_positive"][1] - TABLE4_GALACTIC["previous_positive"][1]
    d_l_pos = TABLE4_GALACTIC["new_positive"][0] - TABLE4_GALACTIC["previous_positive"][0]
    d_b_neg = TABLE4_GALACTIC["new_negative"][1] - TABLE4_GALACTIC["previous_negative"][1]
    d_l_neg = TABLE4_GALACTIC["new_negative"][0] - TABLE4_GALACTIC["previous_negative"][0]
    return {
        "mode": "INTERNAL_CONSISTENCY_CHECK_REPORT_ONLY",
        "rows": TABLE4_GALACTIC,
        "positive_horn_delta": {"l_deg": round(d_l_pos, 3), "b_deg": round(d_b_pos, 3)},
        "negative_horn_delta": {"l_deg": round(d_l_neg, 3), "b_deg": round(d_b_neg, 3)},
        "finding": "Positive-horn b changes by +1.04 deg while l changes by only -0.03 deg and the J2000 RA/Dec moved by ~29 arcsec (RA) / ~0 arcsec (Dec): a >1 deg latitude shift is impossible for such a small repositioning within the paper's own table. Negative-horn shifts (l -0.03, b +0.06) behave as expected. Suspected typographical error in the new positive-horn b (plausible intent: -18.85). Status AMBIGUOUS; flagged, not resolved.",
    }


def run_all() -> dict:
    freq = reproduce_frequency_chain()
    freq["status"] = "AGREE" if freq["absolute_difference"]["f_channel2_mhz"] < 1e-3 else "DISAGREE"
    data_check = verify_2lo_in_frozen_data()
    flux = reproduce_flux_arithmetic()
    galactic = galactic_consistency_check()
    results = {
        "run_date_utc": "2026-08-23",
        "authorization": "Phase A explicit authorization 2026-08-23 (frequency chain + flux arithmetic only)",
        "source_of_record": {"arxiv": "2508.10657", "version": "v1", "tex": str(PAPER_TEX.relative_to(ROOT)).replace("\\", "/"),
                             "repository_commit": "28624a1eaf955ced940db347684cee61c8e4fd61"},
        "frequency_chain": freq,
        "frequency_data_level_check": data_check,
        "flux_arithmetic": flux,
        "galactic_consistency_check": galactic,
        "not_attempted": [
            "position/squint corrections (private Aug 16 1977 strip chart dependency)",
            "velocity transforms (outside authorized scope; convention ambiguities documented in evidence vector)",
            "Gaussian beam fit, EVT, OCR (outside authorized scope)",
        ],
    }
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(results, indent=2), encoding="utf-8")
    return results


def main() -> None:
    results = run_all()
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
