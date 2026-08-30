# Ellingsen/Hobart Archive — Documentation Extraction (README-First Pass)

Status: **forensic, read-only** · Date: 2026-08-25 · Gate: BLOCKED (human review required)

This document extracts every scientific statement obtainable from the donor
documentation and embedded file headers of
`research/sources/ellingsen_hobart/original/`, classifying each as
**DOCUMENTED** (stated in donor material), **INFERRED** (derived here from
content, with reasoning), or **UNKNOWN**. No inference is ever promoted to a
documented fact.

Sources used in this pass:

| Source | Path (under `original/`) |
|---|---|
| Top-level README (1998–99 era) | `drive-download-20260825T053211Z-1-001/README` |
| 2010 campaign README | `…-001/2010obs/README` |
| 2013 campaign README | `…-001/2013obs/README` |
| ASAP extraction script | `…-001/2010obs/wow.py`, `…-001/2013obs/wow.py` |
| Reduction log (calibration) | `…-001/2010obs/ricky_10228.log` |
| Acquisition logs | `bruce_10228.log`, `bruce_13189.log`, `bruce_13192.log`, `bruce_14205.log` |
| Spectrum dump headers | 81,913 ASAP ASCII headers (indexed: `analysis/spectrum_header_index.csv`) |
| FITS/RPFITS headers | `data/*.fit.gz`, `2010obs/bruce_10228.fit`, `*.rpf` |
| SAS plot headers | `*.gsf.gz` PostScript comments |

---

## 1. Telescope and site

- **DOCUMENTED**: telescope is Mt Pleasant 26 m (`TELESCOP = 'MT_PLEASANT'`,
  site cards SITELAT −42.803866°, SITELONG 147.440019°, SITEELEV 63.67 m in
  `bruce_10228.fit`; UTAS fourier live-pages database referenced in the 2013
  README).
- **DOCUMENTED**: receiver/spectrometer is the UTAS correlator
  (`ORIGIN='UTAS'/'UTAS 26m'`, `INSTRUME='CORRELATOR'`). The 2013 README shows
  positions were pulled from the `mt_pleasant_26` database on
  `fourier.phys.utas.edu.au`.
- **UNKNOWN**: receiver noise temperatures, backend number of IFs beyond the
  two used, feed polarization details beyond "linear".

## 2. Observing frequencies and spectral configurations

- **DOCUMENTED** (2010): observing at 1420 MHz; calibrator scans taken with
  bandwidth 16 MHz per IF (`ricky_10228.log`: "frequency, bandwidth:
  1420.000000, 16.000000"; `BANDWIDT = [16, 16]` in bruce_10228.fit).
  Program dumps: 2048 channels × 976.5625 kHz ⇒ **2 MHz** per configuration
  (header WCS lines), TOPO frequency abcissa in MHz, rest frequency
  1.42041 GHz.
- **DOCUMENTED** (2013/14): field-session dumps use 2048 × 1953.125 kHz ⇒
  **4 MHz**. Test sessions DOY 189–198 use the 976.5625 kHz spacing; DOY 199
  onward switches to 1953.125 kHz (INFERRED from header census; the switch
  itself is not narrated anywhere).
- **DOCUMENTED**: two linear polarizations exported per cycle ("Pol Type:
  linear", pol1/pol2 files).
- **INFERRED**: the 1998–99 `.fit.gz` products store 1024-lag autocorrelation
  functions ("ACF", unit COUNTS) per extension; spectra require an FFT with a
  documented lag/window convention. Neither lags-to-channel mapping nor
  bandwidth is recorded in the files.
- **UNKNOWN**: usable/passband edges, Doppler tracking conventions per era,
  velocity definition.

## 3. Campaign timelines

### 3.1 1998–99 correlator era (top-level README + filenames)

- **DOCUMENTED** sessions (all positions B1950):
  - DOY 76/77 (1999): 19 22 22 −27 18 00, on-source 076-14:54:05 → 077-05:04:00;
    *off-source 22:12–22:19 UT because the Y drive was accidentally left off
    during maintenance* (X/Y offsets tabulated in the README).
  - DOY 77: 19 25 12 −27 18 00, 15:02:13 → 23:?? UT; *correlator ran out of
    disk space*.
  - DOY 79/80: same position; 15:02:09 → 04:50:00; *"No known problems"*
    except a concatenation mistake that lost the 02–03 UT data after deletion
    of originals.
  - DOY 81/82: antenna physically at 19 22 22 −26 48 00 but correlator command
    file mislabelled it 19 25 12 −27 18 00 → *~1.5 kHz Doppler error* in
    reported velocities for that day (variation only 36 Hz across the run).
  - DOY 91/92: ACT crashed during observation; last log entry 23:00:00 UT;
    end time uncertain.
  - DOY 99/100: *"Observations appear to have gone OK."*
- **DOCUMENTED**: top-level README scopes itself to "data collected between
  1999 076 – 100", yet `data/` also contains w98278xx–w98282xx (INFERRED:
  1998 Oct 5–9). The 1998 files are not covered by any received narrative.
- **INFERRED**: filename pattern `wYYDOYNNN.fit.gz` encodes year+DOY+sequence;
  internal `DATE` cards are export dates (e.g., 2 days after DOY 076), not
  observation dates.

### 3.2 2010 campaign (README + logs)

- **DOCUMENTED**: made *for Michael Jaekle*; data from 11:00 UT "through until
  about 15:42 UT when I had to hand the telescope over for the VLBI
  experiment".
- **DOCUMENTED**: antenna drive system froze at 12:54 UT, reboot needed,
  back observing ~13:25 UT; correlator kept running; *"I suspect that the
  antenna was off source from 12:54"* (last live-page timestamp quoted).
- **DOCUMENTED calibration chain** (README numbers reproduced exactly by
  `ricky_10228.log`):
  - calibrator 3C348; assumed flux 46.52 Jy at 1420 MHz "according to Ott et al."
  - IF#1: Source/CAL 0.899/0.917/0.973/0.978 → CAL = 49.4 Jy; SEFD/CAL
    9.010/9.120/9.151/9.149 → SEFD = 450 Jy
  - IF#2: Source/CAL 0.866/0.848/0.897/0.852 → CAL = 53.7 Jy; SEFD/CAL
    8.080/…/8.065 → SEFD = 433 Jy
  - measured beam FWHM 33.8′–36.8′ across 8 cross-scans (both IFs)
- **DOCUMENTED** (bruce_10228.log): session began JD 2455424.639 (03:20 UT)
  with unrelated NGC6334 work at 6669 MHz, Hydra A pointing checks, then
  `frequency 1420` + `source 3c348` at ~10:00 UT, park at ~10:27 UT.
- **INFERRED** (headers): program spectra span 09:31:38–15:42:33 UT on
  2010-08-16; three RPFITS archives map to outputs file1/file2/file3
  (c102280930/c102281100/c102281325) per the README's wow.py usage lines.
- **DOCUMENTED**: pointing 19:23:03 −26:43:24 (J2000-labelled) with named
  off-position pairs wow_off1 (−25:43:24) and wow_off2 (−27:43:24), ±1° in Dec.

### 3.3 2013/2014 campaigns (logs, tarball names, headers, positions extracts)

- **DOCUMENTED** (README): how pointing extracts were obtained (MySQL query on
  the live-pages DB) and how tarballs were packed (`find . -name '*.txt' |
  tar -cvzf … --files-from -`).
- **INFERRED** session table (from tarball names + header times):

| Session | UTC span (first→last spectrum) | Content |
|---|---|---|
| test doy189 | 2013-07-08 12:38 → (doy189) | freq-1420 checks; Hydra A region |
| test doy192 | 2013-07-11 12:26 → … | "wow" @ 19:25:28 −26:57, 2 MHz config |
| test doy198 | 2013-07-17 … | "wow"/zenith mix, 2 MHz config |
| test doy199 | 2013-07-18 12:38 → 15:05 | first 4 MHz config |
| field1 doy218 | 2013-08-06 05:25 → … | "wow_f1" @ 19:25:28 −26:57 |
| field2 doy219 | 2013-08-07 05:21 → 19:34 | "wow_f2" @ 19:28:17 −26:57 |
| field1 doy256 | 2013-09-13 … | "wow_f1" |
| field1 doy258 | 2013-09-15 … ends 03:39 | "wow_f1" |
| field2 doy205 | 2014-07-24 06:17 → 15:19 | "wow_f2" |
| field1 doy283 | 2014-10-10 01:11 → 10-11 07:26 | "wow_f1" |

- **DOCUMENTED**: acquisition logs confirm control-software sessions on
  JD 2456481.67 (2013-07-08), 2456484.72 (2013-07-11), 2456862.72 (2014-07-24)
  with attenuator states, `frequency 1420`, Hydra A/Hydra pointing checks.
- **DOCUMENTED**: live-pages extracts show the antenna genuinely tracked RA
  19:28:17 on one 2013 day and 19:25:28 on the 2014-10 day (dominant entries
  in the 04–21 UT windows), confirming two distinct commanded pointings.

## 4. Data processing and detection criteria

- **DOCUMENTED** (wow.py, both versions): per-scan, per-cycle, per-pol ASCII
  export via ASAP `scantable(...)`; 2010 version scales by fixed CAL factors
  (49.4 / 53.7 Jy); 2013 adds `wow_extract_fixtsys` scaling to nominal
  Tsys = 500 K using per-cycle `get_tsys()`.
- **DOCUMENTED**: dumps carry x = TOPO MHz and y0/yf0 columns; yf0 is 0 in all
  inspected samples (role UNKNOWN — possibly a fitted/flagged column).
- **DOCUMENTED** (.gsf.gz PostScript comments): Bob Gray's SAS 6.12/WinNT
  PROC GPLOT diagnostics dated Sep 26 – Oct 10 1998:
  `PLOT OF COUNT * SIGMA_RD`, `BUBBLE OF TIME * CHANNEL = SIGMA_P` (×2),
  `PLOT OF MAX_SIG * CHANNEL`.
- **UNKNOWN / NOT IN ARCHIVE**: detection thresholds, candidate-selection
  rules, RFI flagging criteria, repeat-detection criteria for ANY era; no
  candidate lists or follow-up decision records are included.

## 5. File formats

- **DOCUMENTED** (Simon, via directive): .gsf are statistical-package output;
  .fit are a Hobart-specific non-standard format.
- **VERIFIED BY INSPECTION**: .rpf carry the literal signature
  `SIMPLE = F / NONCONFORMIST` + `FORMAT = RPFITS` (ATNF RPFITS);
  `bruce_10228.fit` is standards-conformant FITS (astropy-readable,
  'SINGLE DISH' BINTABLE, 51 columns); `data/*.fit.gz` are conformant FITS
  wrappers around ACF binary tables whose headers carry no observational
  metadata (the practical sense of "non-standard").

## 6. Explicit unknowns carried forward

Detection thresholds · RFI treatment · integration/dump timing within scans ·
band-limits and bandpass shape · Doppler/velocity frame handling · 2013/14
absolute flux scale · completeness of the transfer · whereabouts of any
written follow-up analyses for 2010/2013/2014 · meaning of yf0 column ·
identity/purpose of `spectra.tar.gz` beyond verified duplication.
