# HOBART GAP STATUS — v2 (Round 2 close-out)

Date: 2026-08-25 · Companion: `LOCAL_HOBART_GAP_AUDIT.md`,
`research/data/ellingsen_gap_register.yaml` (v1.1).
Labels: **ESTABLISHED** (multi-source archive fact) · **REPRODUCED**
(independent arithmetic re-run) · **DERIVED** (computed, locator-cited) ·
**INFERRED** (interpretation, flagged) · **UNKNOWN** · **DONOR-DEPENDENT**.

## Corrections to Round-1 state (evidence-superseded)

| Item | Was | Now | Basis |
|---|---|---|---|
| Field1/Field2 intent | OPEN ("epoch error" vs two-locale hypotheses) | RESOLVED: deliberate East/West Big-Eam beam locales with documented B1950↔J2000 pairs | ESTABLISHED via plan workbook 'Wow Details' sheet |
| Session bandwidths | DERIVED 2/4 MHz "from 2048-ch headers" | 4/8/16 MHz at 4096 ch/pol | ESTABLISHED via rpf NAXIS4/CDELT4 + workbook Observations sheet; ASAP-export 2048-ch discrepancy registered as GAP-HOB-018 (OPEN) |
| 2013/14 calibrators possibly inside .rpf | possible (class B) | EXCLUDED for supplied files | ESTABLISHED negative result, wide-window SU scan |
| Dump integration | UNKNOWN | planned Tint = 5 s documented; executed value still unconfirmed | ESTABLISHED (plan) + DONOR-DEPENDENT tail |
| Session dates from filenames only | DERIVED convention | OBS date card in every .rpf | ESTABLISHED |

## Current status of all gaps (register v1.1)

| Gap | Status |
|---|---|
| 001 completeness | UNKNOWN / DONOR-DEPENDENT |
| 002 field1 intent | RESOLVED (plan doc) |
| 003 field2 intent | RESOLVED (plan doc) |
| 004 2010 position rationale | PARTIALLY_RESOLVED → DONOR-DEPENDENT core |
| 005 thresholds | OPEN (plan-stage procedures known; executed rules DONOR-DEPENDENT) |
| 006 candidate selection | OPEN (same split) |
| 007 RFI semantics | OPEN (intended excision documented; executed unknown) |
| 008 repeat criteria | OPEN / DONOR-DEPENDENT |
| 009 outcomes | OPEN / DONOR-DEPENDENT (+ G&E2002 OCR pending authorization) |
| 010/011 2013/14 calibration | OPEN, class C-leaning; rpf-calibrator route excluded |
| 012 1998–99 config | OPEN / DONOR-DEPENDENT (conversion TECHNICALLY POSSIBLE / SCIENTIFICALLY UNVERIFIED) |
| 013 rpf↔session mapping | RESOLVED (SU + OBS cards) |
| 014 integration time | PARTIALLY_RESOLVED (planned 5 s) |
| 015 beam model | PARTIALLY_RESOLVED (1-D FWHM measured; 2-D UNKNOWN) |
| 016 campaign-era error box | OPEN / DONOR-DEPENDENT (workbook gives Ohio State beamwidths + historical freq/flux variants — recorded, not adopted) |
| 017 publication relationship | PARTIALLY_RESOLVED (G&E2002 identity verified; post-2010 status DONOR-DEPENDENT) |
| 018 channel-count discrepancy (NEW) | OPEN |

## H5 safeguard status

Unchanged and enforced: exposure ≠ selection function; file counts, durations,
Jy labels, absence-of-candidates, nominal Tsys, and beam FWHM are each
insufficient for any likelihood ingredient. R5–R10 remain MISSING; the formal
H5 path stays BLOCKED. No likelihood, prior, Bayes factor, posterior,
efficiency, or rate parameter exists in this branch (guard-tested).

## Prohibitions compliance check (§10)

All upheld this round: no inference quantities emitted; no calibration
promotion (C-leaning labels intact); no cadence→integration conversion
(plan citation required and given); no non-detection statements; no
completeness claims; no spatial weights (geometry labeled DESCRIPTIVE /
NON-INFERENTIAL); Méndez vector hash re-verified by tests; originals
untouched (full-suite hash verification); legacy results untouched.
