# Hobart Calibration Reconciliation

Date: 2026-08-25 · Scope: MASTER DIRECTIVE §9–10 · **No extrapolation to
2013/2014 is made anywhere in this document.**

## 1. The 2010 chain — formal arithmetic reproduction

Every input below is quoted with locator; every output recomputed this pass.

**Step 1 — calibrator flux assumption (paper-stated constant).**
`S_3C348(1420 MHz) = 46.52 Jy` — `original/…-001/2010obs/README`, line
"Calibration on 3C348. At 1.420 GHz flux density is 46.52 Jy according to Ott
et al." Provenance: DOCUMENTED, second-hand scale ("Ott et al."), not
independently derived in this project.

**Step 2 — eight Source/CAL ratios** (`ricky_10228.log`, fields
"Source/cal, err"; identical values embedded in `bruce_10228.fit` TSYS columns
as SEFD/CAL counterparts):
IF#1: 0.899, 0.917, 0.973, 0.978 · IF#2: 0.866, 0.848, 0.897, 0.852.

**Step 3 — CAL in Jy.**
mean_IF1 = 0.941750 → CAL₁ = 46.52 / 0.941750 = **49.398 Jy** (README: 49.4 ✔)
mean_IF2 = 0.865750 → CAL₂ = 46.52 / 0.865750 = **53.737 Jy** (README: 53.7 ✔)

**Step 4 — SEFD.**
SEFD/CAL ratios (ricky log): IF#1 9.010, 9.120, 9.151, 9.149 (mean 9.1075);
IF#2 8.080, 8.005, 8.108, 8.065 (mean 8.0645).
SEFD₁ = 49.4 × 9.1075 = **449.9 Jy** (README: 450 ✔)
SEFD₂ = 53.7 × 8.0645 = **433.1 Jy** (README: 433 ✔)
Cross-check: `bruce_10228.fit` row TSYS pairs [9.010112, 8.080193] … match the
log's first ratios to ~6 significant figures.

**Step 5 — beam measurement.** Eight FWHM fits on 3C348 cross-scans
(`ricky_10228.log` "FWHM (arcm)"): 36.3, 34.1, 36.8, 33.8 (IF#1); 34.0, 35.5,
34.6, 35.1 (IF#2) → measured range **33.8′–36.8′**. Elevations at fit time
40.16°–41.07° (same lines). 2-D response: UNKNOWN (no map, no illumination
data).

**Step 6 — calibrator-scan noise samples.** "RMS-noise/CAL" per fit:
0.0065–0.0145 → σ ≈ CAL × ratio ≈ **0.32–0.78 Jy** per calibrator scan sample
(IF-dependent). This characterizes the calibrator scans only.

**Step 7 — program-dump scale.** `wow.py` applies
`data.scale(cal1|cal2, tsys=True)` to each polarization before ASCII export
(script header comment: "calibrates it using the scaling factors calculated
above"), so the loose dumps are nominally on the above CAL/Jy scale with the
bandpass still included (y₀ continuum ≈ 215 units visible in headers/data).

## 2. Answer to the directive question

*"Can an independent researcher reconstruct the 2010 sensitivity scale from
the supplied files alone?"* — **YES, for the scale itself**: Steps 1–5 use
only archived artifacts and reproduce every published number to the printed
precision. What is NOT yet reconstructed, and is explicitly deferred:
per-program-dump rms (requires a stated bandpass/baseline convention),
gain-elevation behaviour outside 40°–41°, and any 2-D beam correction. These
are derivable-but-uncomputed, not missing.

## 3. 2013/2014 — meaning of the printed "Jy"

Evidence: the 2013 `wow.py` adds `wow_extract_fixtsys(nomtsys=500)` which does
`data.scale(nomtsys/tsys[0], tsys=True)` per cycle — a normalization to a
nominal 500 K system temperature. No calibrator constant, SEFD, or Jy chain
for 2013/14 exists in the archive; bruce logs show Hydra A checks occurred
(doy189/192), so calibrator integrations may reside inside the `.rpf`
archives, unreadable without RPFITS tooling.

Directive classes:

- A (fully calibrated & reproducible): **NOT SUPPORTED**.
- B (calibrated, constants missing): **POSSIBLE** — hinges on donor records or
  `.rpf` contents.
- C (relative/instrumental normalization despite the Jy label): **MOST
  CONSISTENT with what is archived** — the code path produces
  nominal-Tsys-normalized instrumental units.
- D (undeterminable): **NOT REQUIRED YET**.

Recorded verdict (also in `ellingsen_campaign_metadata.yaml`):
`RELATIVE_NORMALIZATION_PROVISIONAL`, class **C-leaning**, for both 2013 and
2014. Nothing may treat those dumps as absolute flux densities.

## 4. Guardrails encoded

- No number from §3 may be promoted to absolute calibration without new donor
  evidence or decoded calibrator scans (tests enforce the label).
- The ≥256 ±63 Jy Arecibo censored bound is untouched by, and unrelated to,
  anything in this document.
