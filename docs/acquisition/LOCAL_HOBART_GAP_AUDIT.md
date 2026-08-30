# LOCAL HOBART GAP AUDIT — Round 2 (local-only exhaustion before any donor contact)

Date: 2026-08-25 · Directive §3 sections A–I · Everything below is
archive-derived; Simon is assumed unreachable. Labels: ESTABLISHED /
REPRODUCED / DERIVED / INFERRED / UNKNOWN / DONOR-DEPENDENT.

## A. Complete session reconstruction

`extracted/HOBART_SESSION_MASTER_TABLE.csv` (33 rows: 27 RPFITS-archive rows +
6 documented 1998–99 README sessions). Populated fields carry per-row
locators; everything else is literal UNKNOWN.

New per-session facts (all ESTABLISHED from `.rpf` primary-header cards,
`analysis/rpfits_card_inventory.json`):
- `OBS=` date card present in every archive → session dates no longer depend
  on filename conventions alone.
- `OBJECT`, `OBSERVER='Simon'`, `EPOCH='j2000'`, `BUNIT='JY'`.
- Spectral axis per file: CRVAL4 = 1420.000 MHz; CDELT4 ∈ {976.5625 kHz,
  1953.125 kHz}; NAXIS4 = 4097 ⇒ **4096 channels/pol**.
- STOKES axis present; uv-style PTYPE columns (UU/VV) in table section.

## B. RPFITS forensics (keyword-window extraction only; no conversion)

Recoverable per file (ESTABLISHED): observation date, observer, target
names + commanded RA/Dec (SU tables, wide-scan `rpfits_su_widescan.json`),
epoch, units label, frequency axis (center + spacing), Stokes/table layout,
file size.
NOT recoverable without a real RPFITS reader: scan-level timestamps,
integration-time records inside the data stream, backend configuration
detail beyond header cards, antenna state series, calibration scan content.
**Negative result (ESTABLISHED): NO calibrator entries (Hydra A / 3C348 /
planets) exist in ANY supplied `.rpf`** — checked with a widened numeric
window specifically designed to catch them.

## C. Search-procedure forensics

Vocabulary sweep (`thresh|snr|candidate|detect|reject|persist|repeat|
baseline|interference|rfi`) over every README, log, script, and plot:
- Observing logs/scripts/plots: **zero substantive hits** (earlier crude hit
  counts were benign words such as "completed").
- NEW (ESTABLISHED, plan-stage only): the Jaekle workbook documents intended
  procedures — 'Data Analysis' sheet (RFI identification/excision, HI-profile
  subtraction, big-spike search with summary statistics/histograms,
  aggregation from 5-s spectra, optional pulsar-style folding); 'Confirmation
  Options' sheet (on/off target, Doppler-drift, independent confirmation via
  VLA/ATCA/ATA); 'Sensitivity' sheet (Tint = 5.0 s configurations; Tsys
  ≈ 920 Jy worst-case single-pol, ~680 Jy other orthogonal feed; "Simon
  (2012)/(2013) gave…" and "I need Tsys in K" notes).
Classification: these are PLAN-stage intentions by the 2013 requester;
EXECUTED thresholds/rules remain UNKNOWN (DONOR-DEPENDENT).
Explicit distinction maintained: **"no candidate file exists" ≠ "no
candidates existed."**

## D. Calibration forensics (2013/14)

- fixtsys path normalizes to nominal Tsys = 500 K (code) — ESTABLISHED.
- No calibrator scans in any `.rpf` (B above) → class-B-via-rpf **excluded**
  for supplied files.
- Workbook provides planning-level Tsys figures in Jy and an explicit need
  for K-conversion — supports, but does not upgrade, the C-leaning verdict.
Verdict unchanged: **C-leaning provisional**; absolute calibration remains
DONOR-DEPENDENT.

## E. 1998–99 correlator forensics

- Repository-wide search found correlator documentation ONLY in our own
  prior reports (no independent local documentation exists).
- Files remain bare ACF dumps (1024 lags, COUNTS, DATE/ORIGIN/INSTRUME only).
- FFT conversion to spectra: **TECHNICALLY POSSIBLE / SCIENTIFICALLY
  UNVERIFIED** — bandwidth/window/lag-to-channel mapping undocumented
  (GAP-HOB-012 OPEN, DONOR-DEPENDENT).

## F. 2010 calibration reproduction (independent re-run)

Recomputed this round from archived numbers only:
mean Source/CAL IF1 = 0.941750 → CAL₁ = 46.52/0.941750 = 49.398 ✔ (49.4)
mean IF2 = 0.865750 → CAL₂ = 53.737 ✔ (53.7)
SEFD₁ = 49.4×9.1075 = 449.9 ✔ (450); SEFD₂ = 53.7×8.0645 = 433.1 ✔ (433)
FWHM set {36.3,34.1,36.8,33.8,34.0,35.5,34.6,35.1}′ ✔ range 33.8–36.8.
**No discrepancies found** (REPRODUCED).

## G. Pointing / geometry — DESCRIPTIVE / NON-INFERENTIAL

All geometry remains confined to `analysis/pointing_geometry.json` and its
document; no weights or probabilities produced. New context (ESTABLISHED):
the Jaekle workbook's 'Wow Details, etc' sheet lists the two locales as
**"East beam" (B1950 19 22 22 −27 03 ↔ J2000 19 25 28 −26 57)** and **"West
beam" (B1950 19 25 12 −27 03 ↔ J2000 19 28 17 −26 57)** — i.e., the field1/
field2 duality is DOCUMENTED campaign design, resolving GAP-HOB-002/003 at
the intent level without inference. It also gives Ohio State beamwidths
(RA 8′ = 36 s; Dec 40′) and historical frequency/flux variants (Kraus
1420.356; Ehman 1420.4556 MHz; Ehman-2007 54 Jy; Childers 212 Jy; BW <10 kHz)
— recorded for reconciliation, not adopted.

## H. Duplicate / counting audit

`analysis/HOBART_LOCAL_EVIDENCE_MAP.yaml` declares every dataset identity and
the duplication edge (tarball ⇔ loose 2010 dumps) plus derivation edges
(dumps ← rpf). Exposure tables already exclude the tarball row; tests enforce
count-once. No other duplication exists (6,681 unique hashes).

## I. Document / literature forensics

`wow_published.pdf`: hash-frozen and inventoried; identity bibliographically
confirmed (DOI 10.1086/342646). Text is fully vectorized (0 readable streams
of 37). **OCR NOT performed — awaiting human authorization** per directive;
no OCR output exists anywhere in the repository.
