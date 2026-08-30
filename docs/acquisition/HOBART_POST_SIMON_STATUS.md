# Hobart Post-Simon Scientific Status Matrix

Status: **evidence-reconstruction summary; NO inference performed** ·
Date: 2026-08-29 · MASTER DIRECTIVE (2026-08-29) §25 ·
Evidence sources: `research/data/ellingsen_simon_response.yaml` (verbatim
freeze), `research/data/ellingsen_gap_register.yaml` v1.2 (audit trail),
`HOBART_1998_99_FORENSIC_PROCESSING_REPORT.md`.

Epistemic vocabulary (no vague labels):

- `ESTABLISHED_DOCUMENTARY` — multi-source archive/plan fact with locator.
- `ESTABLISHED_DONOR_TESTIMONY` — donor statement of fact/recollection.
- `MEASURED` — independently measured from archived data.
- `DONOR_SUPPORTED` — donor recollection consistent with other evidence;
  not independently proven.
- `DONOR_SPECULATION` — hedged donor statement; UNVERIFIED by definition.
- `NOT_LOCATED` — absent from surviving donor-held material; existence
  elsewhere not excluded.
- `UNRESOLVED` / `UNKNOWN`.

| Evidence layer | Status | Evidence | Quantitative use now? |
|---|---|---|---|
| Archive completeness | `ESTABLISHED_DONOR_TESTIMONY` — complete surviving **donor-held** material; historical completeness UNKNOWN | Q1 verbatim ("This is all there is…"); GAP-001 `RESOLVED_DONOR_SIDE` | NO (and never as "complete historical archive") |
| Pointing (2013/14 fields) | `ESTABLISHED_DOCUMENTARY` (plan workbook) + geometry MEASURED | GAP-002/003; donor could not recall intent beyond plan (Q2) | Geometry only, DESCRIPTIVE; no spatial weighting |
| Pointing (2010) | geometry MEASURED; intent `DONOR_SPECULATION` | GAP-004 round3 amendment (Q4 "I suspect…") | NO (intent unresolved) |
| Epoch conversion (B1950→J2000) | `ESTABLISHED_DONOR_TESTIMONY` + `ESTABLISHED_DOCUMENTARY` | Q3 ("Yes that sounds correct") + plan workbook pairs; epoch-error interpretation retired as primary | NO (interpretive provenance only) |
| Timing | cadence MEASURED (5.0 s median, all sessions); integration `DONOR_SUPPORTED` ≈5 s ("I think") + plan Tint=5.0 s | GAP-014 round3 amendment (Q9) | Cadence: descriptive use; integration: NOT as measured quantity |
| Frequency | 2010/2013/14 WCS axes DOCUMENTED per era; 1998/99 coverage UNRESOLVED | GAP-012 tail; header indices | 2010/13/14: descriptive; 1998/99: NO |
| Beam FWHM | 1-D MEASURED (2010: 33.8′–36.8′, 8× 3C348 cross-scans); 2-D UNKNOWN | GAP-015 | 2010 1-D descriptive only; no 2-D weighting |
| 2010 calibration | `ESTABLISHED_DOCUMENTARY` (chain reproduces from archived artifacts: CAL 49.4/53.7 Jy, SEFD 450/433 Jy) | GAP-004-era forensics; ricky/bruce logs | Descriptive/instrumental; confirmatory use still gated |
| 2013/14 calibration | `PROVISIONAL / DONOR-LIMITED` (donor: not a focus; ≈50% qualitative accuracy — NOT a Gaussian σ) | Q7 verbatim; GAP-010/011 `PROVISIONAL_DONOR_LIMITED` | NO absolute use; relative/instrumental scale only |
| 1998/99 processing | architecture `DOCUMENTED_ONLY` (MPSLPP v1.8 + manual v1.0 frozen); kernels 73/73 `REFERENCED_BUT_MISSING` | Q8 + dependency map; GAP-012 `TECHNICALLY_OPEN` | NO (conversion not historically validated) |
| Detection threshold | `NOT_LOCATED` in donor-held material; attributed to Bob Gray | Q5/Q6; GAP-005 | NO |
| RFI criteria | `NOT_LOCATED` (Row_Flagged semantics UNKNOWN); attributed to Bob Gray | Q5/Q6; GAP-007 | NO |
| Candidate definition | `NOT_LOCATED`; attributed to Bob Gray | Q5/Q6; GAP-006 | NO |
| Repeat criteria | `NOT_LOCATED`; attributed to Bob Gray | Q5/Q6; GAP-008 | NO |
| Search outcomes | `NOT_LOCATED` in donor-held material — **NOT a non-detection** | Q6 verbatim; GAP-009 OPEN (narrowed) | NO |
| Selection function | NOT ESTABLISHED (requires threshold + RFI + candidate + repeat layers) | GAP-005–009; readiness matrix | NO |

## Explicitly preserved distinctions

1. **Completeness:** "complete surviving donor-held material" ≠ "complete
   historical Hobart archive."
2. **Speculation vs fact:** Q4 (2010 candidate) and Q2 ("other ideas") are
   `DONOR_SPECULATION`; they must never become observational claims.
3. **Cadence vs integration:** measured 5.0 s spacing ≠ measured 5 s
   integration.
4. **~50% vs σ:** donor-stated qualitative accuracy ≠ Gaussian uncertainty.
5. **Absence of records vs absence of events:** no surviving candidate/
   search-result record ≠ no candidates / no detections / null result.

## Gate status (unchanged)

`confirmatory_comparison_enabled: false` · H1 blocked · H2
partially_unlocked (no promotion) · H3 blocked · H4 blocked · H5 in_progress
but **not quantitatively estimable** from the Hobart archive. No H5
likelihood, Bayes factor, posterior, non-detection term, or evidence-layer
promotion exists in this round (guard-tested).
