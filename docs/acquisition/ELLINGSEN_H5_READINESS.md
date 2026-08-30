# Ellingsen/Hobart Archive — H5 Usability Audit & Readiness Matrix

Status: forensic · Date: 2026-08-25 · Gate: BLOCKED (human review required)

## Verdict

**Can the Ellingsen/Hobart archive support a campaign-specific H5
detection-efficiency model? — PARTIALLY (2010 only, and not yet sufficient).**

- A. Exposure: **YES for 2010/2013/14 session spans** (header-indexed first→last
  spectrum times; documented incidents bound usable time); PARTIAL for
  1998–99 (README windows; per-file timing absent).
- B. Spatial selection: **PARTIALLY** — pointings and off-pairs are
  established, but the field1/field2 epoch discrepancy and the 2010 pointing's
  relation to the canonical Wow! error box are unresolved, and no 2-D beam map
  exists (single-axis FWHM measured in 2010 only).
- C. Spectral selection: **PARTIALLY** — TOPO frequency axes per dump exist
  (2 MHz config 2010/tests; 4 MHz from DOY 199 onward); heliocentric-frame
  handling per session is undocumented; 1998–99 frequency coverage is NOT
  recoverable without external correlator configuration.
- D. Sensitivity: **PARTIALLY for 2010** (SEFD/CAL documented → noise DERIVABLE
  once bandpass handling is fixed); NOT_ESTABLISHED for 2013/14 (nominal-Tsys
  normalization without a Jy chain); UNKNOWN for 1998–99.
- E. Detection threshold: **NO** — no threshold or candidate-selection rule is
  archived for any era.
- F. RFI selection: **NO** — no masking/flagging records (a `Row_Flagged`
  header field exists; semantics unknown).
- G. Repeat-detection process: **NO** — nothing documents how a repetition
  would have been recognized, verified, or reported.
- H. Calibration: **YES for 2010** (documented chain + artifacts);
  NO otherwise.
- I. Uncertainty propagation: **NO** end-to-end — ingredient-level errors are
  partially recoverable (2010), but threshold/selection uncertainties have no
  basis.

## Readiness matrix

| Requirement | Status | Evidence | Scientific consequence |
|---|---|---|---|
| Campaign dates | VERIFIED | logs/tarball names/header times (2010, 2013, 2014); README (1999) | exposure windows usable |
| Observing exposure | PARTIALLY VERIFIED | header index spans + documented incidents (drive freeze, VLBI handover, disk-full, ACT crash, lost concatenation) | usable-time bounds, not exact on-source seconds |
| Pointings | VERIFIED (as commanded) | dump headers + live-pages extracts | geometry known |
| Beam/coverage | PARTIALLY VERIFIED | 2010 FWHM 33.8′–36.8′ (8× 3C348 cross-scans); no 2-D map | 1-D weighting possible for 2010 only |
| Frequency coverage | PARTIALLY VERIFIED | WCS lines per dump | per-session spectral window; frame conversion undocumented |
| Sensitivity | PARTIALLY VERIFIED (2010 only) | SEFD 450/433 Jy, CAL 49.4/53.7 Jy | noise floor derivable for 2010 dumps |
| Detection threshold | MISSING | absent from all documentation | cannot convert spectra to detections/non-detections |
| RFI treatment | MISSING | absent (Row_Flagged semantics UNKNOWN) | contamination model unquantified |
| Candidate selection | MISSING | absent | selection function incomplete by definition |
| Non-detection record | UNVERIFIED | archive contains data, not statements of search outcome | non-detection claims require donor/project records |
| Calibration | VERIFIED (2010) / MISSING (others) | README+ricky+bruce_10228.fit vs fixtsys-only | 2010 flux scale usable; others relative only |
| Uncertainty | MISSING (end-to-end) | partial ingredients only | no defensible error propagation yet |
| Repeat-detection model | MISSING | absent | H5 likelihood cannot be conditioned on this archive yet |

## What the archive *could* contribute to H5 (after gaps close)

1. Session-level exposure windows (when the locale was observed, at what
   spectral resolution) for a temporal-coverage kernel.
2. A measured beam size (2010) anchoring spatial weights.
3. A calibrated 2010 spectrum set (81,913 dumps overall) enabling an
   independent sensitivity/noise characterization of Mt Pleasant follow-ups.
4. Bounding context: what signal classes were in principle observable given
   bandwidth/resolution/polarization coverage.

## What it cannot contribute today

Detection thresholds · RFI/candidate-selection rules · any statement that "no
repeat was found" · any 1998–99 spectral calibration · any 2013/14 absolute
flux scale · confirmation of which pointing actually covered the Wow! locale.

## Kipping & Gray relationship

Question A (reproducing the published Kipping & Gray computational result,
including the documented kmax=100 vs grid-loop ~150/160 Fortran
normalization/extrapolation issue) is **independent** of Question B
(reconstructing Hobart follow-up constraints). Nothing in this archive forces
or tests 1.78% vs 1.42%; the Ellingsen material is observational input to a
*follow-up selection function*, not to the restricted-model emulator. The two
validations must be completed separately before any interaction is modeled.
No attempt was made in this phase to steer either toward agreement with the
other.
