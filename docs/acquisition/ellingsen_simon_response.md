# Simon Ellingsen Donor Response — Human-Readable Freeze

Status: **FROZEN PROVENANCE RECORD** · Date: 2026-08-29 ·
MASTER DIRECTIVE (2026-08-29) §2 · Machine-readable twin:
`research/data/ellingsen_simon_response.yaml` ·
Gap-register effect: `research/data/ellingsen_gap_register.yaml` v1.2
(audit block `simon_response_round_2026_08_29`).

## Provenance

- **Donor:** Simon Ellingsen (University of Tasmania; donor of the Hobart archive).
- **Channel:** answers relayed **verbatim** by the project owner (human) to the
  executing agent on 2026-08-29. The original email is **not locally
  archived**; date/headers/recipient are recorded as UNAVAILABLE.
- **Rule applied:** Simon's wording is preserved; the epistemic strength of
  each answer is preserved and never silently upgraded (directive §1.3).

## Answers (verbatim) and scientific status

### Q1 — Completeness of the archive

> "This is all there is, if I don't have a copy, no one else will have it."

**DONOR_SIDE_SURVIVING_ARCHIVE_COMPLETENESS_RESOLVED.** This is all surviving
material known to/available from Simon. It is **not** established as the
complete historical Hobart archive. GAP-HOB-001 → `RESOLVED_DONOR_SIDE`.

### Q2 — 2013/14 observing fields (intent)

> "I can't remember. Bob Gray had a couple of other ideas that we tested some
> of those would have been with a newer and better correlator system than we
> had in 1998/1999. I don't have access to the emails that we would have
> exchanged in setting up the experiment."

**DONOR_CANNOT_RECALL_INTENT.** The "other ideas" clause is speculation-grade
context, not evidence of what was tested or why. Additional recollections:
2013/14 used a newer correlator than 1998/99; setup emails inaccessible.
Affects GAP-HOB-002/003 (residual), 016, 012 context.

### Q3 — 2013/14 coordinate system

> "Yes that sounds correct"

**DONOR_SUPPORTED_B1950_TO_J2000_INTERPRETATION.** Combined with the
observing-plan workbook (the primary documentary evidence), the epoch-error
interpretation is retired as the primary explanation. Simon has NOT
independently confirmed the scientific motivation of the fields beyond the
plan workbook. GAP-HOB-002/003 amended.

### Q4 — 2010 pointing strategy

> "No, I suspect we may have been following up a candidate from an earlier
> observation."

**UNVERIFIED_DONOR_SPECULATION.** Must not be treated as evidence that a
candidate existed, that 2010 was a repeat detection, that the Wow! Signal was
re-detected, or that H5 repeatability was demonstrated. The 2010 pointing
rationale remains UNRESOLVED. GAP-HOB-004 amended.

### Q5 — Search and detection procedure

> "Bob Gray did all the processing and analysis of the data, I simply
> collected it."

**SEARCH_LAYER_ATTRIBUTED_TO_BOB_GRAY** (donor testimony). Simon is the
data-collection donor; the missing search-layer evidence likely belongs to
Bob Gray or other surviving project records. This is **not** evidence of a
null result. GAP-HOB-005/006/007/008 →
`CLOSED_AS_UNRECOVERABLE_FROM_THIS_DONOR` (redirected to Bob Gray route).

### Q6 — Candidate events and search results

> "I don't have ready access to anything other than what I provided yesterday"

**HISTORICAL_CANDIDATE_RECORD_NOT_LOCATED_IN_DONOR_HELD_MATERIAL.** This is
**not** a statement that no candidates existed. Whether candidates existed,
how many, whether rejected and why, whether any event passed the criteria,
whether a formal null result was issued, and whether the search was complete
all remain unknown. No Bob Gray contact information was provided. GAP-HOB-009
narrowed (stays OPEN).

### Q7 — 2013/14 calibration and flux units

> "I don't think we focused on obtaining accurate calibration, so the
> intensity numbers I wouldn't trust to more than about 50% accuracy."

**ABSOLUTE_CALIBRATION: PROVISIONAL / DONOR-LIMITED.** The "approximately
50%" figure is a qualitative limitation from memory — it is **not** a Gaussian
1σ uncertainty and must not be encoded as σ = 50% without independent
statistical justification. The 2013/14 "Jy" labels are not promoted to
class-A absolute calibration; the Arecibo/Méndez evidence vector is untouched.
GAP-HOB-010/011 → `PROVISIONAL_DONOR_LIMITED`.

### Q8 — 1998/99 autocorrelator software

> "I've attached the high-level fortran program and some partial
> documentation for the software which was used to process data from the
> 1998/99 time. I can't quickly find any of the subroutines/librariries which
> are where the technical stuff is located."

**HIGH_LEVEL_SOFTWARE_SUPPLIED_KERNELS_MISSING** (donor typo preserved).
Supplied artifacts frozen (hashes verified):
`software/mpslpp.f` (MPSLPP v1.8, 5,023 lines) and `documentation/mpslpp.tex`
(MPSLPP User Manual v1.0). GAP-HOB-012 → `TECHNICALLY_OPEN`. See
`HOBART_1998_99_FORENSIC_PROCESSING_REPORT.md`.

### Q9 — Spectral-dump cadence

> "I think that it was a 5 second record for each sample"

**DONOR_SUPPORTED_TIMING_INFORMATION.** Distinction preserved: observed dump
cadence = independently measured (5.0 s median, every session); integration
time = donor-supported ≈5 s ("I think"), consistent with the plan-workbook
Tint = 5.0 s but not exact independent proof. GAP-HOB-014 amended.

## Not addressed in this round

Session-date execution confirmation (v2-Q1) · export decimation 4096→2048
(v2-Q9, GAP-HOB-018 cause) · publication status of the 2010–2014 efforts
(v2-Q11, GAP-HOB-017 tail). All remain OPEN / donor-dependent.

## Standing prohibitions (unchanged)

No Bayesian inference of any kind derives from this response; no non-detection
is inferred; no speculation is promoted; the five-way comparison stays
disabled (`confirmatory_comparison_enabled: false`).
