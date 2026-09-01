# GE2002 — Proposed Gap Register Amendment (v1.2 → v1.3)

Status: **APPLIED to `research/data/ellingsen_gap_register.yaml` (audit block
`ge2002_extraction_round`)** · Directive §9 · Historical states preserved.

## Basis

Text-layer extraction of the frozen Gray & Ellingsen (2002) PDF
(`research/data/ge2002_extraction.yaml`, `ge2002_search_outcome.yaml`).
All changes are **era-split**: the 1998/99 campaign becomes
paper-documented; the 2010/2013/14 campaigns are unchanged and remain
Bob-Gray-dependent.

## Changes applied

| Gap | v1.2 state | v1.3 state | Basis (paper) |
|---|---|---|---|
| GAP-HOB-005 thresholds | CLOSED_AS_UNRECOVERABLE_FROM_THIS_DONOR | **RESOLVED_LOCAL_1998_99** / OPEN 2010–14 | 5.9σ (P_e=0.05); 6.2σ combined; 15.7–18 Jy (Table 3) |
| GAP-HOB-006 candidate rules | CLOSED_AS_UNRECOVERABLE_FROM_THIS_DONOR | **RESOLVED_LOCAL_1998_99** / OPEN 2010–14 | threshold + manual inspection + RFI presumption (§3.3) |
| GAP-HOB-007 RFI semantics | CLOSED_AS_UNRECOVERABLE_FROM_THIS_DONOR | **RESOLVED_LOCAL_1998_99** / OPEN 2010–14 | off-source sampling, median smoothing, bridging (§2.1/2.3/3.3); Row_Flagged (2013/14) still UNKNOWN |
| GAP-HOB-008 repeat criteria | CLOSED_AS_UNRECOVERABLE_FROM_THIS_DONOR | **RESOLVED_LOCAL_1998_99** / OPEN 2010–14 | period <14 hr detectable; P>0.90 to ~20 hr (§3.4/§4, Fig. 3) |
| GAP-HOB-009 search outcomes | OPEN (narrowed) | **RESOLVED_LOCAL_1998_99** / OPEN 2010–14 | PUBLISHED NON-DETECTION (abstract/§3.3/§4); `PUBLISHED_RESULT_WITHOUT_SURVIVING_CANDIDATE_LEVEL_DATA` |
| GAP-HOB-012 1998/99 config | TECHNICALLY_OPEN | **PARTIALLY_RESOLVED_LOCAL** / TECHNICALLY_OPEN | Table 1 per-field frequencies + Table 2 configuration; kernels still missing |
| GAP-HOB-016 error box | OPEN | OPEN (1998/99 definition documented) | B1950 dual-position ±5 s/±20′, Kraus priv. comm. (§2) |
| GAP-HOB-017 publication link | PARTIALLY_RESOLVED | **RESOLVED_LOCAL_1998_99** / UNKNOWN 2010–14 | content verified: sessions/DOYs/instrument match archive |

## Explicitly NOT changed

- GAP-HOB-001/004/010/011/013/014/015/018 (no paper bearing, or donor-era items).
- The frozen Arecibo/Méndez evidence vector (§11: comparison only).
- `confirmatory_comparison_enabled` (stays `false`).
- No historical round-3 states deleted; all prior amendments preserved in place.
