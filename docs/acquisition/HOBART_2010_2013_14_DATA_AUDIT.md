# Hobart 2010 / 2013 / 2014 Campaigns — Authoritative Data-Layer Inventory

Status: **consolidation; NO inference, NO spatial weighting** · Directive
Part 6 · Every item labeled: **ARCHIVED** (observed archival fact) ·
**MEASURED** (derived from archived data) · **DONOR** (donor recollection) ·
**DERIVED** (deterministic calculation) · **INFERRED** · **UNKNOWN**.

## 1. 2010 campaign (2010-08-16, for Michael Jaekle)

| Item | Value | Class | Locator |
|---|---|---|---|
| Date/session | 2010-08-16; data 11:00–15:42 UT (VLBI handover end) | ARCHIVED | 2010obs/README |
| Incident | antenna drive freeze 12:54–13:25 UT (correlator kept running; antenna suspected off-source from 12:54) | ARCHIVED (README narrative) | 2010obs/README |
| Raw data | 3 RPFITS archives: c102280930, c102281100, c102281325 | ARCHIVED | rpfits_source_table_index.json |
| Pointing | wow = 19:23:03 −26:43:24 (J2000-labelled) + off1/off2 at ±1° Dec | ARCHIVED | SU tables |
| Pointing intent | UNKNOWN rationale; donor speculation only ("suspect… following up a candidate") | DONOR (speculation) | simon_response Q4 |
| Frequency config | exports 2048 ch × 976.5625 kHz (2 MHz) TOPO; raw/XLS era 4096 ch — 4 MHz | ARCHIVED + DERIVED | header index; workbook |
| Calibration | 3C348 = 46.52 Jy (Ott et al.); CAL 49.4/53.7 Jy (IF1/IF2); SEFD 450/433 Jy — **arithmetic reproduced from archived artifacts** | ARCHIVED + DERIVED | ricky_10228.log + bruce_10228.fit |
| Beam | 1-D FWHM 33.8′–36.8′ (8× 3C348 cross-scans); 2-D UNKNOWN | ARCHIVED/MEASURED | reduction log |
| Analysis products | 6,500 calibrated ASCII spectra (wow.py, fixed CAL scaling); also inside spectra.tar.gz (byte-identical) | ARCHIVED | 2010obs/ |
| Search records | NONE (no threshold/candidate/outcome record) | UNKNOWN | GAP-005–009 (2010 era) |
| Publication | UNKNOWN | UNKNOWN | GAP-017 |

## 2. 2013/2014 campaigns (test + field sessions, newer correlator)

| Item | Value | Class | Locator |
|---|---|---|---|
| Sessions | tests DOY 189/192/198/199 (2013 Jul); field1/field2 DOY 218/219/256/258 (2013), 205/283 (2014) | ARCHIVED | tarball names + header index |
| Pointings | field1 = 19:25:28 −26:57 (East beam locale); field2 = 19:28:17 −26:57 (West); deliberate B1950→J2000 conversions | ARCHIVED + DONOR-SUPPORTED | plan workbook; Simon Q3 |
| Raw config | 4096 ch/pol (NAXIS4), spacing 976.5625→1953.125 kHz from DOY 199; i.e. 4/8 MHz (+16 MHz calibrator scans) | ARCHIVED | rpfits card inventory; workbook |
| Export discrepancy | ASCII exports declare 2048 ch — decimation step undocumented | ARCHIVED inconsistency | GAP-HOB-018 |
| Cadence | 5.0 s median inter-dump spacing, every session | MEASURED | dump_spacing_stats.json |
| Integration | plan Tint = 5.0 s; donor: "I think… 5 second record" — NOT independently measured | DONOR + ARCHIVED (plan) | GAP-HOB-014 |
| Calibration | NO calibrator scans in any supplied .rpf; exports normalized to nominal Tsys = 500 K ("Jy" label provisional); donor: not a focus, ≈50% qualitative accuracy (NOT σ=50%) | ARCHIVED (code path) + DONOR | GAP-HOB-010/011 |
| Analysis products | 75,413 processed ASCII spectra in tarballs | ARCHIVED | 2013obs/ |
| Search records | NONE for any session | UNKNOWN | GAP-005–009 |
| Publication | UNKNOWN | UNKNOWN | GAP-017 |
| Correlator generation | "newer and better correlator system than… 1998/1999" | DONOR (corroborated by archive parameters) | Simon Q2 |

## 3. Cross-era invariants (never mixed)

- 1998/99: one-bit ACF, 512 ch/pol, 2.5 MHz, 30 s integration, MPSLPP-lineage
  processing, published search + non-detection.
- 2010/2013/14: RPFITS raw, larger channel counts, 5 s cadence, ASAP/python
  exports, **no published or archived search layer**.
- The GE2002 published outcome covers **only** the 1998/99 era
  (DIRECTLY_STATED scope); it says nothing about these campaigns
  (NOT_STATED).

## 4. Known contradictions / unresolved intent

1. Channel-count discrepancy 4096 vs 2048 (2013/14 exports) — cause UNKNOWN
   (GAP-018; likely ASAP behavior; Bob is not the relevant source).
2. 2010 pointing rationale — unresolved (donor speculation only, GAP-004).
3. Executed-vs-plan session/date confirmation (2013/14) — never confirmed by
   donor (v2-Q1 unanswered).
4. "Flux Unit: Jy" in 2013/14 exports must not be read as absolute
   calibration beyond the documented fixtsys/Tsys=500 K evidence; the ≈50%
   figure stays qualitative (NOT a Gaussian σ).
