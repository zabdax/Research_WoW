# Hobart Remaining Gaps After GE2002 + Simon Response

Status: **consolidation audit; register v1.3 authoritative** · Directive
Part 3 · Sources: gap register v1.3 (audit trails intact), Simon response
freeze, GE2002 extraction/search-outcome, MPSLPP forensic inventory.

## Classification vocabulary

RESOLVED · PARTIALLY_RESOLVED · DONOR_DEPENDENT · BOB_DEPENDENT ·
TECHNICALLY_BLOCKED · SCIENTIFICALLY_NON_IDENTIFIABLE · OPTIONAL.
"Required for H5" = without it the 2010–14 selection function / likelihood
cannot be defensibly built. "Required for 1998/99 reconstruction" = without
it the historical data-product/processing reconstruction cannot proceed.

## Master matrix (gaps 001–009)

| Gap | Original question | Current status | Status-changing evidence | Remaining uncertainty | Classification | Req. for H5 | Req. for 1998/99 recon | Ask Bob | Do NOT re-ask |
|---|---|---|---|---|---|---|---|---|---|
| 001 Archive completeness | Is the transfer everything surviving? | Donor-held material complete; historical completeness UNKNOWN | Simon Q1 ("This is all there is…") | Material held by others (e.g., Bob) | RESOLVED (donor scope) + BOB_DEPENDENT (extension) | Indirect | No | Yes — folded into the P0 ask | Do not re-ask Simon |
| 002 Field-1 intent | Why 19:25:28 −26:57 (2013/14)? | Deliberate East-beam locale + B1950→J2000 donor-supported | Plan workbook; Simon Q3 | Motivation beyond plan | RESOLVED | No | No | No | Do not ask (resolved) |
| 003 Field-2 intent | Why 19:28:17 −26:57? | Deliberate West-beam locale; same basis | Plan workbook; Simon Q3 | Motivation beyond plan | RESOLVED | No | No | No | Do not ask (resolved) |
| 004 2010 pointing intent | Why 19:23:03 −26:43:24? | Geometry known; intent unresolved; Simon speculation recorded | Geometry + Simon Q4 (UNVERIFIED_DONOR_SPECULATION) | Whether a prior candidate motivated it | BOB_DEPENDENT | Only if 2010 enters selection function | No | Yes — P1 (one-line context) | Do not press Simon |
| 005 Detection thresholds | What S/N threshold? | **1998/99 RESOLVED_LOCAL** (5.9σ/6.2σ, P_e=0.05, Table 3); 2010–14 unknown | GE2002 §3.2–3.3+Table 3 | Executed 2010–14 thresholds | 1998/99 RESOLVED; 2010–14 BOB_DEPENDENT | **YES** (2010–14) | No (published for 1998/99) | Yes — P0 | 1998/99 thresholds — published |
| 006 Candidate rules | What made a candidate? | **1998/99 RESOLVED_LOCAL** (qualitative); 2010–14 unknown | GE2002 §3.3 | Executed 2010–14 rules; 1998/99 executed deviations | 1998/99 RESOLVED (published level); 2010–14 BOB_DEPENDENT | **YES** (2010–14) | Partial | Yes — P0 (2010–14); P1 (executed 1998/99) | Do not ask what the paper states |
| 007 RFI semantics | RFI/flagging rules; Row_Flagged meaning | **1998/99 RESOLVED_LOCAL** (procedure); Row_Flagged (2013/14) UNKNOWN | GE2002 §2.3/§3.3 | Row_Flagged semantics; 2010–14 rules | 1998/99 RESOLVED; 2010–14 BOB_DEPENDENT; Row_Flagged TECHNICALLY_BLOCKED locally | **YES** (2010–14) | No | Yes — P0 (2010–14) | 1998/99 procedure — answered |
| 008 Repeat criteria | Was a repeat required? | **1998/99 RESOLVED_LOCAL** (period constraint published); 2010–14 unknown | GE2002 §3.4/§4 | 2010–14 repeat logic | 1998/99 RESOLVED; 2010–14 BOB_DEPENDENT | **YES** (2010–14) | No | Yes — P0 (2010–14) | 1998/99 constraint — answered |
| 009 Search outcomes | Any candidates/detections/null? | **1998/99 RESOLVED_LOCAL: PUBLISHED NON-DETECTION** (without candidate-level data); 2010–14 UNKNOWN | GE2002 abstract/§3.3/§4 | 2010–14 outcomes; 1998/99 full candidate list | 1998/99 RESOLVED (published); 2010–14 BOB_DEPENDENT | **YES** (2010–14) | Partial | Yes — P0 | Whether 1998/99 detected anything — published |

## Master matrix (gaps 010–018)

| Gap | Original question | Current status | Status-changing evidence | Remaining uncertainty | Classification | Req. for H5 | Req. for 1998/99 recon | Ask Bob | Do NOT re-ask |
|---|---|---|---|---|---|---|---|---|---|
| 010 2013 calibration | Absolute flux chain? | PROVISIONAL / DONOR-LIMITED (≈50% qualitative; NOT σ) | Simon Q7; fixtsys code path | Any better constants/records | DONOR_LIMITED + BOB_DEPENDENT | Yes (2013 flux scale) | No | Yes — P1 | Do not re-ask Simon; never encode σ=50% |
| 011 2014 calibration | Same for 2014 | PROVISIONAL / DONOR-LIMITED | Simon Q7 (collective) | Same | DONOR_LIMITED + BOB_DEPENDENT | Yes (2014 flux scale) | No | Yes — P1 | — |
| 012 1998/99 correlator config | Config/lag→channel conversion? | Configuration RESOLVED_LOCAL (Tables 1–2); executed software + mapping UNKNOWN | GE2002 Tables 1–2; MPSLPP inventory (73/73 kernels missing) | Kernels, INCLUDEs, version, lag mapping | PARTIALLY_RESOLVED + TECHNICALLY_BLOCKED (kernels) | Indirect | **YES** | Yes — P1/P2 | Configuration values — published |
| 013 RPFITS↔session mapping | Which file = which session? | RESOLVED | SU/OBS card inventory | — | RESOLVED | No | n/a (2010–14) | No | Do not ask |
| 014 Integration time | Measured vs planned dumps? | 1998/99: 30 s (paper); 2013/14: cadence 5.0 s measured, ≈5 s DONOR_SUPPORTED, plan Tint=5 s | GE2002 Table 2; dump-spacing stats; Simon Q9 | Executed 2013/14 integration proof | PARTIALLY_RESOLVED | Minor | No | Optional (P2) | Do not re-ask Simon |
| 015 Beam model | 2-D response? | 1-D FWHM measured (2010: 33.8′–36.8′); paper-era 28′ (1998/99); 2-D UNKNOWN | ricky log cross-scans; GE2002 Table 2 | 2-D beam any era | PARTIALLY_RESOLVED | Yes (spatial response) | Partial | Optional (P2) | — |
| 016 Error box | Which box did campaigns target? | 1998/99 definition published (B1950 dual-position ±5 s/±20′); 2010–14 targeting unrecorded | GE2002 §2 | 2010–14 targeting; relation to Arecibo II locales (HISTORICAL DIFFERENCE, unresolved) | PARTIALLY_RESOLVED + BOB_DEPENDENT | Yes (spatial term) | No | Yes — P1 | 1998/99 definition — answered |
| 017 Publication link | Were campaigns published? | 1998/99 → G&E 2002 RESOLVED_LOCAL (content verified); 2010–14 UNKNOWN | GE2002 extraction | Any 2010–14 reports/theses | RESOLVED (1998/99) + BOB_DEPENDENT (2010–14) | No | No | Yes — P2 | 1998/99 link — answered |
| 018 Channel-count discrepancy | 4096 raw vs 2048 exported (2013/14)? | Cause UNKNOWN (undocumented ASAP export step) | Header census vs XLS | The decimation step | TECHNICALLY_BLOCKED (locally) | Minor | No | Optional (P2 — likely an ASAP behavior question, not Bob-specific) | — |

## Summary counts

- **RESOLVED (locally):** 002, 003, 013, 017(1998/99), and 005/006/007/008/009
  (1998/99 era)
- **PARTIALLY_RESOLVED:** 004(geometry), 012, 014, 015, 016
- **DONOR_LIMITED:** 010, 011
- **BOB_DEPENDENT (blocking H5):** 005/006/007/008/009 (2010–14 era) — the P0 set
- **TECHNICALLY_BLOCKED:** 012 (kernels), 018 (locally)
- **SCIENTIFICALLY_NON_IDENTIFIABLE today:** H5 selection function for any
  era (pending P0 recovery); the 1998/99 selection function is partially
  recoverable from published parameters only
- **OPTIONAL:** 014 confirmation, 015 2-D beam, 018, ancillary P3 material

## Historical states

All prior amendment blocks (round-1/2 workbook era, round-3 Simon response,
round-4 GE2002) remain in `research/data/ellingsen_gap_register.yaml`
unchanged. This document is a read-only consolidation, not a register edit.

