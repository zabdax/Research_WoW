# Bob Gray — Remaining Information Requirements (post-GE2002)

Status: PREPARED (internal) · Consolidation phase · **Verified minimum
information set** — every item below was checked against the repository
(gap register v1.3, GE2002 extraction, Simon freeze, MPSLPP inventory)
rather than assumed. Supersedes the pre-paper
`bob_gray_information_requirements.md` for scope. **DO NOT CONTACT —
separate human-controlled phase.**

## Necessity test applied

An item is P0 only if its absence **genuinely blocks** the next scientific
calculation (the 2010–14 selection function and the audit of the published
1998/99 outcome). Items already answered by the paper or Simon were removed
(see `bob_gray_do_not_ask_again.md`).

## Context update from the GE2002 extraction

The paper establishes (DIRECTLY_STATED): Robert H. Gray (Gray Data
Consulting, Chicago) performed the 1998/99 analysis with Ellingsen;
processing used "a modified version of the observatory spectral line
analysis software (Ellingsen 1996)"; the search applied 5.9σ/6.2σ
thresholds (P_e=0.05), off-source RFI screening, median-smoothed/bridged
references, a running H i baseline, and reported a **published
non-detection** with two described candidate features and a period
constraint (>14 hr; P>0.90 to ~20 hr at nominal positions).

What the paper does NOT establish drives the list below.

## P0 — scientifically decisive (gates any quantitative selection function)

1. **2010/2013/14 search procedure and outcome.**
   - Why: the paper covers 1998/99 only; the later campaigns' thresholds,
     candidate rules, RFI handling, repeat criteria, and outcomes are
     entirely unknown (`NOT_STATED` in paper; absent from archive; Simon
     holds nothing).
   - Evidence available: archive data + plan workbook (intended procedures
     only); Simon Q5/Q6.
   - Minimum ask: any surviving record of thresholds/candidate handling/
     outcomes for 2010/2013/14 — including "none was done" or "nothing
     survives".
   - Prohibited if unanswered: any H5 quantity from the later campaigns.

2. **1998/99 candidate-level data.**
   - Why: the paper describes only two features; the full list of
     threshold-passing features (before/after RFI rejection) is
     `PUBLISHED_RESULT_WITHOUT_SURVIVING_CANDIDATE_LEVEL_DATA`. Needed to
     verify the published outcome against the raw archive and to build any
     candidate-rate model.
   - Minimum ask: candidate lists/working files/summary tables, including
     rejected items, or confirmation that none survive.

3. **Executed processing parameters vs published description.**
   - Why: the paper describes the pipeline (quotient, running baseline,
     bridged references, cubic baseline) but not the executed software
     version or exact parameters; MPSLPP kernels are missing, so the
     published description cannot be independently executed.
   - Minimum ask: software version used; processing scripts/notes; whether
     published Table 2/§2.1 parameters were exactly executed.

## P1 — materially useful

4. **Missing software**: MPSLPP subroutines/libraries (READFIT, WRITEFIT,
   VANVLECK, DOFFT, HANNING, SVDFIT, GAUFIT…), INCLUDE files, the MPSLPP
   Programming Manual — would enable verified data-product reconstruction
   (currently DEPENDENCY_MISSING).
5. **Lag→channel mapping and window convention** for the 1024-lag ACFs
   (paper gives 512 ch/pol, 4.88 kHz spacing, Hanning — the mapping itself
   is INFERRED, not documented).
6. **RFI channel lists / flagging records** from the 1998/99 reduction
   (which channels were ignored, per run).
7. **Figure data** for G&E 2002 Fig. 3 (detection probability vs period) —
   would upgrade `FIGURE_VALUE` caption-level knowledge to quantitative
   curves.

## P2 — useful historical forensics (no quantitative impact)

8. Correspondence with Kraus/Dixon/Ehman cited in the paper's
   acknowledgments (provenance of the B1950 coordinates and the ~60 Jy flux
   estimate).
9. Relationship between the 1998/99 work and the 2010 Jaekle observation.
10. Any later re-analyses or re-examinations of the 1998/99 Hobart data.

## P3 — optional ancillary material

11. Historical observing notes/logs from the 1998/99 runs beyond the
    published summary (context only; the published record is already
    scientifically sufficient for the outcome statement).
12. Copies of the OSU working materials referenced in the paper
    (Ehman 1998 working paper; Dixon/Cole beam geometry) — context only.
13. Any photographs/records of the 1998/99 correlator configuration.

None of P3 affects identifiability; request only if the contact occurs and
Bob offers.

## Verification trail (repository check per P0 item)

| P0 item | Verified absent from | Checked in |
|---|---|---|
| 2010–14 search procedure/outcome | archive READMEs, logs, wow.py, plan workbook (intended-only), all extraction reports | gap register GAP-005–009 (2010–14 era CLOSED_AS_UNRECOVERABLE_FROM_THIS_DONOR / OPEN) |
| 1998/99 candidate-level data | paper (two features only), donor archive (no candidate files), G&E extraction | `ge2002_search_outcome.yaml` candidate_catalogue_status |
| Executed 1998/99 parameters | paper (published description only), MPSLPP manual (v1.0 ≠ source v1.8), Simon Q8 (libraries missing) | `ellingsen_fortran_inventory.yaml` (73/73 REFERENCED_BUT_MISSING) |

## Answered by GE2002 (do NOT re-ask)

1998/99 session dates/positions/frequencies (Table 1) · instrument
configuration (Table 2) · thresholds (Table 3) · RFI and candidate
procedure (§2.3/§3.3) · published outcome and period constraint ·
calibration chain (Virgo A, noise diode) · software lineage (Ellingsen
1996) · Robert H. Gray's identity/role and affiliation.

## Standing rules

- "Nothing survives" is a useful, recordable answer.
- He is not asked to reproduce decades-old analysis or infer from memory.
- Any surviving files can be supplied in any convenient form.
- **No contact has been made and none will be made without explicit human
  authorization.**
