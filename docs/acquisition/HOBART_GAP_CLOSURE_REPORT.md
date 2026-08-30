# HOBART GAP-CLOSURE REPORT

Date: 2026-08-25 · Phase: gap closure + H5 readiness ·
**STOPPED before any inference. Five-way posterior remains disabled; Arecibo
evidence vector untouched (hash-verified).**

Artifacts produced this phase: `ellingsen_gap_closure_questions.md`,
`hobart_literature_reconciliation.md`, `hobart_nondetection_status.md`,
`hobart_h5_readiness.md`, `hobart_pointing_reconciliation.md`,
`hobart_calibration_reconciliation.md`, `research/data/ellingsen_gap_register.yaml`
(GAP-HOB-001…017), `ellingsen_coordinate_provenance.yaml`,
`ellingsen_campaign_metadata.yaml`, plus analysis JSONs
(`pointing_geometry.json`, `rpfits_source_table_index.json`,
`dump_spacing_stats.json`, `gsf_text_tokens.json`, `rpfits_header_probe.json`).

## 1. What did the archive definitively establish?

- Full RPFITS→session→commanded-pointing map for all 27 `.rpf` archives, with
  instrument-side `EPOCH='j2000'` cards (GAP-HOB-013 RESOLVED).
- Geometry: field1 = 5.8′ from the positive-horn locale, field2 = 4.9′ from
  the negative-horn locale; both equal the precessed images of the documented
  1999 B1950 grid points to <2 s of time. The 2010 ON position lies ~30′ from
  the positive-horn locale.
- Dump cadence 5.0 s median across every session (spacing, not integration).
- The 2010 calibration chain reproduces to printed precision from archived
  artifacts alone (CAL 49.4/53.7 Jy; SEFD 450/433 Jy; FWHM 33.8′–36.8′).
- Bibliographic identity of the era publication: Gray & Ellingsen 2002,
  ApJ 578:967–971, DOI 10.1086/342646 (Crossref-verified); local PDF is the
  same page-range but unreadable without OCR.
- `spectra.tar.gz` is byte-duplicate packaging of the loose 2010 dumps
  (count-once rule encoded).

## 2. What did it definitively rule out?

- That the field positions are mutually inconsistent or erroneous commands:
  they are coherent, DB-confirmed, J2000-processed pointings matching a
  deliberate-looking two-locale pattern.
- That the 2013/14 "Jy" labels document absolute calibration: the code path
  normalizes to nominal Tsys=500 K (verdict C-leaning provisional).
- That duplicate tarballs add independent exposure.
- That any threshold/RFI/candidate/outcome documentation exists locally for
  2010–2014 (exhaustive search; high confidence of absence).

## 3. What remains unknown?

Completeness of the transfer; session-level observing intent; detection
thresholds; candidate rules; RFI semantics; repeat criteria; true search
outcomes; dump integration times; 2-D beam; 1998–99 correlator configuration;
the error-box definition used by the campaigns; G&E 2002 content; whether
post-2002 analyses exist.

## 4. Which gaps can be solved locally?

Already closed this phase: GAP-HOB-013 (mapping), geometry halves of 002/003/
004, cadence half of 014, 1-D half of 015. Potentially solvable locally next:
per-dump noise statistics for 2010 (derivable, deliberately not computed this
phase), and OCR of `wow_published.pdf` if tooling is authorized.

## 5. Which require Simon/Ellingsen or another historical source?

001 completeness · intent cores of 002/003/004 · 005 thresholds · 006
candidate rules · 007 RFI semantics · 008 repeat criteria · 009 outcomes ·
010/011 calibration constants · 012 correlator config · 016 error-box
definition used then · 017 existence of post-2002 reports (question set sent
as drafted).

## 6. Which are fundamentally unrecoverable?

None are *proved* unrecoverable. At-risk-if-delayed: 1998–99 correlator
configuration (012) and 2010–2014 outcome recollections (009) depend on
human memory and fragile media; treat as perishable evidence.

## 7. Minimum evidence required to unlock H5?

Per `hobart_h5_readiness.md`: explicit outcomes or a fully documented search
procedure for ≥1 campaign (closes R5/R7/R9/R10), RFI semantics (R6), a written
signal-class definition (R14), era-appropriate calibration closure (R4/R13),
and intent resolution or human waiver for the pointing gaps (R2). Until then
H5 likelihood construction stays BLOCKED.

## 8. What can be stated in an RNAAS manuscript now?

Safe now: the archive's existence/contents and internal consistency; the
measured 33.8′–36.8′ Mt Pleasant beam at 1420 MHz (2010); the reproducible
2010 CAL/SEFD scale; the geometric finding that the 2013–14 field pair
brackets both horn locales within ~5–6′ and matches precessed 1999 grid
points to <2 s; the pointing-epoch caution itself (documented ambiguity).
Not safe yet: any sensitivity-based exclusion, non-detection claim, repetition
constraint, or H5 number.

## 9. What must remain explicitly blocked?

H5 likelihood/prior/Bayes-factor/five-way posterior/campaign-rate
marginalization; promotion of any Hobart quantity into the formal evidence
layer; treatment of 2013/14 dumps as absolute fluxes; spatial weighting before
the intent gate; non-detection statements of any kind; resurrection of legacy
scores. `confirmatory_comparison_enabled` stays false; the Arecibo/Méndez
freeze stands (sha256 re-verified by tests).

---

**HUMAN AUTHORIZATION REQUIRED BEFORE ANY NEXT PHASE.**
