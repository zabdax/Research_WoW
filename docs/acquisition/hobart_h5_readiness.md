# Hobart H5 Readiness Matrix (R1–R14)

Date: 2026-08-25 · Scope: MASTER DIRECTIVE §13 · Supersedes the provisional
matrix in ELLINGSEN_H5_READINESS.md where they differ.
**Formal H5 likelihood: BLOCKED.** Statuses: VERIFIED / PARTIAL / MISSING.

| # | Component | Status | Basis |
|---|---|---|---|
| R1 | Observation exposure | PARTIAL | Session windows triple-sourced (headers/logs/live-pages); true usable time bounded by incidents only; 1998–99 coarse |
| R2 | Pointing / beam response | PARTIAL | Commanded pointings + SU tables + DB extracts VERIFIED; beam = measured 1-D FWHM (2010) only; 2-D UNKNOWN; intent gaps 002–004 open |
| R3 | Frequency coverage | PARTIAL | Per-dump TOPO axes + two configs (2/4 MHz) VERIFIED; heliocentric-frame handling undocumented; 1998–99 unrecoverable without correlator config |
| R4 | Sensitivity | PARTIAL | 2010 scale reproducible (calibration_reconciliation §2); per-dump rms derivable-not-computed; 2013/14 relative-only; 1998–99 none |
| R5 | Detection threshold | MISSING | Not in archive (GAP-HOB-005) |
| R6 | RFI / flagging | MISSING | Semantics absent; Row_Flagged unexplained (GAP-HOB-007) |
| R7 | Candidate selection | MISSING | No rules archived (GAP-HOB-006) |
| R8 | Repeat criterion | MISSING | Nothing defines how a repetition would count (GAP-HOB-008) |
| R9 | Search completeness | MISSING | Which fraction of recorded time was actually searched is unknown (GAP-HOB-014/009) |
| R10 | Explicit outcome | MISSING | No outcome statements for any campaign (GAP-HOB-009); G&E2002 content unverified |
| R11 | Campaign independence | PARTIAL | Duplicate packaging resolved (count-once rule); cross-era instrument drift unresolved (single telescope/family assumed, not documented) |
| R12 | Temporal relationship | PARTIAL | Session datetimes VERIFIED; their relation to any H5 repetition process is model-side and deliberately not assumed |
| R13 | Calibration uncertainty | MISSING | Only 2010 partially grounded; error budget unbuilt |
| R14 | Signal-class definition | MISSING | "Wow-like repeat" never operationally defined for these instruments |

## Minimum sufficient set to unlock H5 (proposal to the human gate)

H5 cannot move while R5–R10 are all MISSING. Minimum path:

1. Explicit search-outcome records OR a fully documented search procedure for
   at least one campaign (closes R5/R7/R9/R10 together — donor round Priority 2).
2. RFI/flagging semantics (R6) from the same documentation.
3. A written definition of the counted signal class (R14) consistent with the
   project's censoring rules.
4. For whichever campaign is used: era-appropriate calibration closure
   (2010 derivable now; 2013/14 needs donor constants or decoded `.rpf`
   calibrators) → R4/R13.
5. Intent resolution or explicit human waiver for GAP-HOB-002/003/004 → R2.

Until then: no likelihood, no efficiency number, no Bayes factor, no posterior
input — nothing from this archive enters H5 quantitatively.
