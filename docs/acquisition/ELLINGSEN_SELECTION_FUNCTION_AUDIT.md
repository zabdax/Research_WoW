# Ellingsen/Hobart — Follow-Up Selection-Function Audit

Status: forensic audit only · **No detection efficiency is computed here** ·
Date: 2026-08-25

Question addressed (per MASTER DIRECTIVE §14): *given the observational setup
reconstructed from this archive, what class of repeat signals could each
campaign have detected?* We identify which ingredients of

```
P(detection | signal properties, campaign conditions)
```

exist in the archive, which are derivable, and which are missing. The equation
itself is **not implemented**.

---

## 1. Ingredient status by campaign era

Statuses: AVAILABLE (in-archive, verified) · PARTIALLY_AVAILABLE · DERIVABLE
(obtainable from archived material by explicit work) · MISSING (not in
archive; must be acquired) · UNKNOWN (cannot currently judge).

| Ingredient | 1998–99 | 2010 | 2013/14 |
|---|---|---|---|
| Sky coverage (pointings vs time) | PARTIALLY_AVAILABLE (README session positions B1950; no per-scan positions in files) | AVAILABLE (dump headers + live-pages + logs) | AVAILABLE (dump headers + positions extracts) |
| Beam response | MISSING | AVAILABLE (measured FWHM 33.8′–36.8′, 8 cross-scans on 3C348, both IFs) | PARTIALLY_AVAILABLE (same feed/dish presumed — INFERRED, not re-measured in-archive) |
| Frequency coverage | NOT_RECOVERABLE from files alone (ACF lags, no freq cards); MISSING correlator config | AVAILABLE (TOPO MHz axis per dump; 2048×976.5625 kHz ≈ 2 MHz) | AVAILABLE (2048×1953.125 kHz ≈ 4 MHz; config change between DOY 198→199 DOCUMENTED by headers) |
| Integration time / duty cycle | UNKNOWN | PARTIALLY_AVAILABLE (dump spacing recoverable from header times; true dump integration UNKNOWN) | PARTIALLY_AVAILABLE (same caveat) |
| Sensitivity (σ in flux units) | UNKNOWN | PARTIALLY_AVAILABLE: SEFD 450/433 Jy + CAL 49.4/53.7 Jy documented; per-dump noise DERIVABLE from dumps after bandpass handling is fixed | NOT_ESTABLISHED: `fixtsys` path normalizes to nominal Tsys=500 K; no Jy chain documented |
| Detection threshold (what counted as a candidate) | MISSING (plots show σ-based diagnostics but thresholds undocumented) | MISSING | MISSING |
| Candidate verification / follow-up decision records | MISSING | MISSING | MISSING |
| RFI masking / rejection | MISSING | MISSING | MISSING (Row_Flagged header line exists but semantics UNKNOWN) |
| Polarization response | PARTIALLY_AVAILABLE (two linear pols exported; relative calibration UNKNOWN) | same | same |
| Pointing accuracy / offsets | PARTIALLY_AVAILABLE (README X/Y drive incident tabulated for 1999; bruce offset checks exist for 2010–14 sessions) | AVAILABLE in principle (bruce/ricky offset prints) | PARTIALLY_AVAILABLE |
| Epoch/coordinate interpretation | DOCUMENTED B1950 usage | **CRITICAL OPEN ITEM** (see §2) | **CRITICAL OPEN ITEM** (see §2) |
| Calibration (absolute flux) | MISSING | AVAILABLE (full chain documented + archived artifacts) | MISSING (nominal-Tsys normalization only) |

## 2. Critical open item — field1/field2 pointing epoch

Established facts (documented):
- Two commanded pointings were used at Dec −26°57′: RA 19:25:28 ("field1",
  wow_f1 dumps) and RA 19:28:17 ("field2", wow_f2 dumps). Both dump headers
  and the live-pages DB label them J2000; the antenna demonstrably tracked
  both values.
- The measured 2010 beam FWHM is ~34–37 arcmin.

Flagged inference (NOT a conclusion): the commonly cited Wow! position
(B1950 ≈ 19h25m, Dec −26°57′ region) precesses to J2000 ≈ 19h28m; "field2"
matches that precessed position while "field1" equals the literal un-precessed
B1950 numbers. If field1 was intended as the Wow! locale but commanded without
precession, its beam center sits ΔRA = 2m49s ≈ 37′ (≈1 FWHM) from the locale,
and beam response at the locale would be strongly attenuated. This affects
which sessions constrain H5-type repeats and **must be resolved with the donor
or project documentation before any exposure weighting**.

The 2010 pointing (J2000-labelled 19:23:03 −26:43:24, ±1° Dec off-pairs) is
likewise tens of arcminutes from the cited locale; intent (grid point inside
the error box vs epoch mix-up) is UNKNOWN pending reconciliation against the
canonical Wow! error box.

## 3. Non-detection is not zero

No statement of the form P(no detection | H5) = 0 or any equivalent appears in
project material, and none may be derived from these archives. Any future use
of these campaigns as non-detection constraints requires the full integral
over signal-rate model × exposure × detection efficiency × selection effects,
with the ingredient gaps above closed first.

## 4. Campaign information vs H5 model assumptions

| Quantity | Observationally established here | H5 model assumption (never to be conflated) |
|---|---|---|
| Session dates/times | yes (headers/logs/README) | — |
| Pointing centers & off-pairs | yes (headers/live-pages) | — |
| Bandwidth/channelization | yes (header WCS lines) | — |
| Beam FWHM | yes, 2010 measurement | shape beyond measured Gaussian summary |
| Flux calibration | 2010: documented chain | — |
| Sensitivity σ | derivable in part (2010) | — |
| Detection threshold | MISSING | threshold distribution |
| Repetition rate / event process | — | H5 model parameter |
| Source lifetime / luminosity function | — | H5 prior |
| Number of accessible repeat sites | — | H5 population model |

## 5. Bottom line

A campaign-specific detection-efficiency model is **partially reconstructable
for 2010** (geometry, spectral window, beam size, and flux scale all present;
missing only threshold/RFI/candidate-selection rules) and **not yet
reconstructable for 1998–99 and 2013/14** (calibration and/or configuration
gaps; plus the unresolved pointing-epoch issue affecting all eras' spatial
weights). No numerical P(detection|…) may be produced from this archive until
the MISSING items are supplied or explicitly bounded by human-authorized
assumptions.
