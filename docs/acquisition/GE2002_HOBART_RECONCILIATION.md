# GE2002 ↔ Hobart Archive ↔ MPSLPP ↔ Simon — Reconciliation

Status: **historical reconciliation; no evidence-layer promotion** ·
Directive §7/§8/§11 · Sources: `research/data/ge2002_extraction.yaml`,
frozen Hobart archive, gap register v1.2, Simon response freeze, Arecibo II
frozen extraction (comparison only).

## 1. Master reconciliation table

| Topic | 2002 paper | Archive | MPSLPP/docs | Simon | Status |
|---|---|---|---|---|---|
| 1998/99 session dates | 1998 Oct 5/9; 1999 Mar 17/18, 20/21, 22/23, Apr 9/10 (Table 1, DOY 278/282/76-77/79-80/81-82/99-100) | `.fit.gz` w98278xx…w9910004; 1999 README lists same DOYs | — | — | **CONSISTENT** (paper↔archive filename/DOY match) |
| 1998/99 positions | 19h22m22s / 19h25m12s ±5 s, −27°03′±20′ (B1950.0, Kraus priv. comm. 1990) + ±15′ fields | 1999 README grid points (same B1950 values); donor workbook B1950↔J2000 pairs | — | "Yes that sounds correct" (2013/14 = converted from these B1950 positions) | **CONSISTENT + COMPLEMENTARY** |
| Beam-locales lineage | two positions = dual-feed ambiguity (OSU ±difference, no sign) | workbook East/West beam locales; 2013/14 field1/field2 | — | — | **CONSISTENT** (2013/14 fields track the same two locales) |
| 1998/99 correlator | one-bit ACF spectrometer; 512 ch/pol; 4.88 kHz spacing; 2.5 MHz; Hanning → 9.765 kHz; 30 s integration; Tsys 1200 Jy (120 K) | `.fit.gz` = 1024-lag ACFs, COUNTS (no config metadata) | `maxlag=1024` source constant; quotient Q=(S/R)−1; Hanning; Van Vleck | — | **COMPLEMENTARY** (paper supplies the config the archive lacks; 1024 lags→512 ch consistent but mapping INFERRED) |
| 1998/99 processing software | "modified version of the observatory spectral line analysis software (Ellingsen 1996)" | — | MPSLPP v1.8 (1993–95), author Ellingsen; kernels missing | supplied mpslpp.f + manual; cannot locate subroutines/libraries | **COMPLEMENTARY; executed version UNKNOWN** (paper doesn't name MPSLPP/version — Bob P1) |
| Van Vleck correction | not named; 1-bit β/2 sensitivity factor | — | VANVLECK kernel present as call | — | **COMPLEMENTARY** (different vocabularies, same correction class; kernel body missing) |
| 1998/99 calibration | Virgo A 211 Jy (Baars); noise diode every 10 min; σ=2.46 Jy/30 s; rms 2.6–3.0 Jy | COUNTS-unit ACFs, no calibration chain archived | — | — | **COMPLEMENTARY** (paper is the missing 1998/99 calibration documentation) |
| Detection threshold | 5.9σ (P_e=0.05) per field; 6.2σ combined; 15.7–18 Jy (Table 3) | no threshold documentation anywhere | — | — | **RESOLVED for 1998/99** (paper); 2010–14 still absent |
| Search outcome 1998/99 | published non-detection (abstract, §3.3, §4); period >14 hr constraint | no candidate/outcome records | — | "Bob Gray did all the processing and analysis" | **RESOLVED for 1998/99** (published); candidate-level data NOT published |
| Search outcome 2010/2013/14 | NOT_STATED (paper predates them) | no records | — | no access | **UNRESOLVED — Bob-Gray-dependent** |
| 1998/99 integration time | 30 s (Table 2) | 1024-lag ACF dumps; no timing metadata | — | "5 second record" (about 2013/14 dumps) | **CONSISTENT — different eras** (30 s for 1998/99; 5 s for 2013/14; Simon's remark was about the later data) |
| HPBW | 28′ (Table 2, 1998/99) | 2010 measured FWHM 33.8′–36.8′ (8× 3C348 cross-scans) | — | — | **APPARENT CONFLICT — era-level**: different epochs/configurations; both preserved; no resolution attempted |
| 1999 incidents | footnote a: 1925S2 (DOY 79/80) "1 hr missing mid-run" | README: lost concatenation 02–03 UT Mar 20/21 | — | — | **CONSISTENT** (independent corroboration of archive README) |
| 1999 DOY 77 disk-full | not mentioned in paper | README: correlator disk-full Mar 18 | — | — | **COMPLEMENTARY** (archive detail beyond paper; no conflict) |
| Wow flux | ~60 Jy (30σ) historical estimate | — | — | — | **HISTORICAL DIFFERENCE** vs frozen Arecibo II (≥250 Jy lower bound) — flagged, unresolved, Méndez vector untouched |
| Wow frequency | "given by Kraus", ~20 kHz below LSR (=HI peak); OSU 50 channels | — | — | — | **HISTORICAL DIFFERENCE** vs Arecibo II 1420.726 MHz reconstruction — flagged, unresolved |
| Error box | B1950 dual-position ±5 s/±20′ + beam ambiguity (1998/99 working definition) | project-canonical horn locales from Arecibo II Table 4 (J2000) | — | — | **PAPER-LEVEL AMBIGUITY vs modern definition**: different definitions for different eras; both preserved; not adjudicated |
| 2010/13/14 correlator | NOT_STATED | RPFITS 4096 ch/pol, 4/8/16 MHz | — | "newer and better correlator than 1998/1999" | **CONSISTENT** (donor recollection corroborated by archive parameters) |

## 2. Disagreement classification summary

- **Apparent conflict (1):** HPBW 28′ (paper, 1998/99) vs 33.8′–36.8′
  (measured 2010). Era-level difference; not resolved (directive §7).
- **Historical differences (2):** Wow flux (~60 Jy vs ≥250 Jy) and
  frequency-at-HI-peak vs 1420.726 MHz — historical-definition differences,
  preserved side-by-side; the frozen Méndez vector is untouched.
- **No true contradictions found** between paper, archive, MPSLPP, and
  Simon's statements for the 1998/99 era.

## 3. What the paper adds that nothing local previously had

1. The published **non-detection outcome** for the 1998/99 follow-up.
2. The **search thresholds** (5.9σ/6.2σ, P_e=0.05, Table 3 Jy values).
3. The **candidate-handling record** (two features described + RFI
   presumption).
4. The **1998/99 instrument configuration** (Table 2) — filling the
   archive's principal metadata void.
5. The **per-field observing frequencies** (Table 1) — supplying the
   frequency metadata absent from every `.fit.gz` header.
6. The **repeat/period constraint** (<14 hr detectable; P>0.90 to ~20 hr).
7. The **MPSLPP lineage** ("modified version of the observatory spectral
   line analysis software, Ellingsen 1996").
