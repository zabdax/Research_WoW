# Ellingsen/Hobart Dataset Forensics — Final Report

Status: **forensic phase complete; STOPPED before inference** ·
Date: 2026-08-25 · Gate: BLOCKED pending human review (MASTER DIRECTIVE §28)

---

## 1. Executive summary

Simon Ellingsen supplied ~5.8 GB (6.19 GB decimal / 5.76 GiB) in three Google
Drive parts (6,681 files) covering **three distinct eras** of Mt Pleasant
(Hobart, UTAS 26 m) follow-up work:

1. **1998–99 correlator era** (`data/`): 122 gzipped FITS files of 1024-lag
   autocorrelation dumps (w98278xx…w9910004), four Bob Gray SAS/GRAPH
   statistical plots (.gsf.gz, Sep–Oct 1998), a published-paper PDF whose
   metadata matches ApJ 578:967–971, and a README documenting the six 1999
   sessions with their known problems.
2. **2010 campaign** (`2010obs/`): 2010-08-16 follow-up for Michael Jaekle.
   Three RPFITS raw archives, a calibration FITS + reduction log pair that
   reproduces the documented CAL/SEFD/beam-FWHM numbers exactly, the ASAP
   extraction script, and 6,500 calibrated ASCII spectra (also present,
   byte-identical, inside `spectra.tar.gz`).
3. **2013/2014 campaigns** (`2013obs/`): test sessions (2013 July DOY
   189/192/198/199) and field1/field2 sessions (2013 DOY 218/219/256/258;
   2014 DOY 205/283) delivered as RPFITS archives, control logs, live-pages
   pointing extracts, an observing-plan .xls, and tarballs holding 75,413
   processed ASCII spectra.

Total processed spectra across all eras' ASCII products: **81,913**
(6,500 loose + 75,413 tarball members).

The directive's working description ("2010 and 2013 campaigns") is therefore
incomplete: the archive also contains the 1998–99 era and two 2014 sessions.

## 2. Archive integrity

- 6,681 files hashed (SHA-256): **all unique**, zero duplicates at file level,
  zero zero-byte files, zero unreadable files. Total 6,190,451,083 bytes.
- Extension census: txt 6,503 · gz 137 (= 122 `.fit.gz` + 11 `.tar.gz`
  + 4 `.gsf.gz`) · rpf 27 · log 5 · py 2 · fit 1 · xls 1 · pdf 1 ·
  extension-less 4 (three READMEs + `.DS_Store` macOS artifact).
- Member-level duplication verified: `spectra.tar.gz` ↔ loose 2010 txt =
  6,500↔6,500 identical name sets, byte-identical samples (kept both;
  nothing deleted).
- All mtimes are 2026 transfer artifacts; dating uses embedded content only.
- Artifacts: `metadata/file_inventory.csv`, `metadata/inventory_summary.json`,
  `hashes/SHA256SUMS.txt`.

## 3. Provenance

Whole archive DONOR_SUPPLIED. Per-file provisional classes (automated rules +
manual review): RAW_OBSERVATIONAL (.rpf ×27, .fit.gz ×122),
PROCESSED_OBSERVATION (81,913 spectra incl. tarball members as packages),
STATISTICAL_OUTPUT (.gsf.gz ×4), SCAN_METADATA (logs ×5, bruce_10228.fit
calibration product), POINTING_METADATA (positions ×3), DOCUMENTATION
(READMEs, wow.py ×2, .xls), PUBLICATION (PDF), UNKNOWN (.DS_Store;
bruce_10228.fit carries both PROCESSED/CALIBRATION attributes).
Nothing was relabeled RAW without demonstration; the 2010/13 "raw" tier is
RPFITS, not the txt dumps.

## 4. Documentation extraction

See `docs/acquisition/ELLINGSEN_README_EXTRACTION.md`. Headline documented
facts: Mt Pleasant 26 m site cards; UTAS correlator; 1999 session incident log
(Y-drive off 22:12–22:19 UT Mar 17/18, correlator disk-full Mar 18, lost
02–03 UT concatenation Mar 20/21, ~1.5 kHz Doppler error from a mislabelled
command position Mar 22/23, ACT crash Apr 1/2); 2010 drive freeze 12:54→13:25
UT and VLBI handover at 15:42 UT; full 2010 calibration chain (3C348 = 46.52
Jy per Ott et al.; CAL 49.4/53.7 Jy; SEFD 450/433 Jy); ASAP export scripts
with the 2010 fixed-CAL vs 2013 nominal-Tsys(500 K) difference.

## 5. FITS/.fit forensics

- `bruce_10228.fit`: conformant FITS (astropy-readable). Primary
  ORIGIN='UTAS 26m'; one 'SINGLE DISH' BINTABLE, 4 rows = 4× 3C348 cross-scans,
  51 columns (OBJECT/BEAMFWHM/JD-OBS/AZ/EL/weather/FREQUENC/BANDWIDT/
  TSYS/DATA…). FREQUENC unfilled ([0,0]); TSYS columns hold the SEFD/CAL
  ratios matching ricky_10228.log to 3 decimals. BANDWIDT=[16,16] MHz.
- `data/*.fit.gz` (×122, indexed in `analysis/data_fit_index.json`):
  conformant FITS wrappers, primary DATE/ORIGIN/INSTRUME only, then
  DATA.NNNN BINTABLEs each 1024 rows × 'ACF' REAL (COUNTS). HDU counts
  16–117. **No frequency/position/time/bandwidth anywhere in the files** —
  the practical non-standardness is information-free headers plus lag-domain
  data needing the UTAS correlator configuration for spectral conversion.
- `.rpf` (×29 total incl. -002): literal signature `SIMPLE = F /
  NONCONFORMIST`, `FORMAT = RPFITS` → ATNF RPFITS; requires RPFITS-aware
  tooling (ASAP), which this repository does not have. Not parsed beyond
  signatures (read-only policy preserved).
- DATE cards inside w9*.fit.gz are export dates, not observation dates.

## 6. GSF forensics

All four are SAS Institute PROC GPLOT PostScript (SAS 6.12.0045P092697,
Windows NT), gzip-compressed: pl-distr (COUNT*SIGMA_RD, 1998-10-10), sp-pl1
and sp-pl1c (BUBBLE TIME*CHANNEL=SIGMA_P, 1998-10-06 and 1998-09-26),
sp-plt5 (MAX_SIG*CHANNEL, 1998-10-07). Classification: STATISTICAL_OUTPUT
(search-diagnostic plots). They are not likelihoods, event lists, or data.

## 7. Campaign reconstruction

17-session exposure table: `extracted/campaign_exposure.csv` (generated by
`scripts/ellingsen_campaign_exposure.py`). Highlights:
- 1999: six documented sessions (above).
- 2010-08-16: program spectra 09:31:38–15:42:33 UT; calibrator block
  ~10:00–10:27 UT; incident-bounded usable time.
- 2013 tests: Jul 8–18; spectral-config change from 976.5625 kHz spacing
  (DOY ≤198) to 1953.125 kHz (DOY 199 onward).
- Field sessions: field1 @ commanded 19:25:28 −26:57 (Aug 6, Sep 13, Sep 15
  2013; Oct 10–11 2014), field2 @ 19:28:17 −26:57 (Aug 7 2013; Jul 24 2014).

## 8. Spatial coverage

Per-dump pointings harvested (analysis/spectrum_header_index.csv): 2010 on-
position 19:23:03 −26:43:24 with ±1° Dec off-pairs (wow_off1/off2); 2013/14
field1/field2 as above; zenith-labelled records at Dec-shifted strings.
Live-pages extracts independently confirm the antenna tracked 19:28:17 (one
2013 day) and 19:25:28 (2014-10-10). Beam: single-axis FWHM measured only in
2010 (33.8′–36.8′); no 2-D beam map any era.

## 9. Spectral coverage

2048 channels throughout; TOPO-frequency abcissa; rest frequency 1.42041 GHz;
bandwidth 2 MHz (2010 + early tests) or 4 MHz (DOY 199 onward). Heliocentric/
velocity-frame handling undocumented. 1998–99 frequency coverage NOT
recoverable from archived files alone.

## 10. Sensitivity and calibration

- 2010: complete documented chain (calibrator flux assumption → CAL → SEFD →
  scaled Jy dumps) with artifacts; noise floor DERIVABLE from dumps once
  bandpass conventions are fixed. Elevations ~40–41° at cal time.
- 2013/14: `wow_extract_fixtsys` normalizes to nominal Tsys=500 K; no Jy
  chain archived ⇒ absolute sensitivity NOT established despite "Flux Unit:
  Jy" header labels (label provenance unverified).
- 1998–99: UNKNOWN (no calibration material received).

## 11. Detection procedure

Not recoverable for any era: no thresholds, candidate lists, RFI flags,
verification protocols, or outcome statements are included. The SAS plots
show σ-space diagnostics were used in 1998 but their decision rules are not
archived.

## 12. Selection-function audit

See `docs/acquisition/ELLINGSEN_SELECTION_FUNCTION_AUDIT.md`. Summary: 2010 is
partially reconstructable (geometry+spectral window+beam+flux scale present;
threshold/RFI/candidate rules missing); 1998–99 and 2013/14 are not yet
reconstructable; spatial weights for ALL eras depend on resolving §14 below.

## 13. H5 relevance

See `docs/acquisition/ELLINGSEN_H5_READINESS.md`. Verdict PARTIALLY (2010
only, insufficient today). Potential contributions after gaps close: session
exposure windows, measured beam size, independent noise characterization,
observable-signal-class bounds.

## 14. Critical open item — pointing epoch (potential contradiction)

Field1's commanded RA (19:25:28) equals the un-precessed B1950 Wow!-locale
value while field2's (19:28:17) matches the precessed J2000 position; both are
labelled J2000 in headers and DB. With FWHM ≈ 34–37′, if field1 was intended
as the locale it observed through ≈1-FWHM-attenuated response there; field2
would be the on-locale session. The 2010 pointing (19:23:03 −26:43:24) is also
tens of arcminutes from commonly cited values. These are flagged INFERENCES;
resolving intent (donor query or project correspondence) is a prerequisite for
any spatial weighting. This is recorded as a potential contradiction *within*
the archive's own labels, not against external results.

## 15. Uncertainties and unresolved issues

Pointing epoch/intent (§14) · dump integration time & timing reference ·
yf0 column meaning · Row_Flagged semantics · zenith-record purpose ·
heliocentric frame handling · 2013/14 absolute scale · 1998–99 correlator
config · .rpf↔session mapping · completeness of transfer · published-PDF
identity (page-range match only) · positions-file day labeling.

## 16. Data gaps (what is missing)

Detection thresholds and candidate-selection rules (all eras) · RFI/flagging
records · repeat-detection criteria and any search-outcome records · 2-D beam
response · 2013/14 calibration chain · 1998–99 configuration documentation ·
ASAP/RPFITS software environment (referenced but not supplied) · anything
establishing whether the 5.8 GB is the complete Hobart archive.

## 17. Scientific readiness

The archive is inventoried, frozen, classified, and documented well enough to
support a focused acquisition round, but **cannot yet legitimately enter an H5
likelihood**: threshold/selection/calibration ingredients are missing, and no
non-detection statement may be inferred from data files alone.

## 18. Recommended next action

Human review of this report, then (if approved): (a) ask Simon Ellingsen the
targeted questions (pointing epoch intent for field1/field2 and 2010 position;
whether searches had documented thresholds/outcomes; 2013/14 flux-calibration
chain; completeness of transfer; 1998–99 correlator configuration; permission
to receive RPFITS-readable tooling or converted copies); (b) obtain/derive the
Wow! error-box definition to reconcile pointings; (c) only afterwards decide
whether an H5 campaign-selection model is identifiable. No evidence-layer
promotion before (a)–(c).

---

### Reproducibility artifacts produced this phase

| Artifact | Producer |
|---|---|
| metadata/file_inventory.csv, hashes/SHA256SUMS.txt, metadata/inventory_summary.json | scripts/ellingsen_inventory.py |
| analysis/spectrum_header_index.csv, analysis/tarball_census.json | scripts/ellingsen_spectrum_header_index.py |
| extracted/campaign_exposure.csv | scripts/ellingsen_campaign_exposure.py |
| analysis/data_fit_index.json, analysis/campaign_coverage_summary.json | inline forensic passes (recorded in report text) |
| tests/research/test_ellingsen_source_lock.py | freeze/immutability verification |

Originals under original/ remain byte-for-byte unchanged (verified by test
suite re-hashing).
