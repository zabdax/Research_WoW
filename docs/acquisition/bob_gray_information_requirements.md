# Bob Gray Information Requirements

Status: PREPARED (internal; DO NOT CONTACT without explicit human authorization) ·
Date: 2026-08-29 · Phase: post-Simon-response preparation (MASTER DIRECTIVE
2026-08-29 §17)

## Purpose

This document defines the **minimum** information required from Bob Gray to
determine whether the surviving Hobart archive can support quantitative
inference. It asks only for what the archive and Simon's response cannot
establish. Facts already established locally are listed at the end
("Do not re-ask") and MUST NOT be re-requested.

## Attribution of the missing analysis layer

Per Simon's statement (donor response, 2026-08-29, see
`research/data/ellingsen_simon_response.yaml` once frozen):

> "Bob Gray did all the processing and analysis of the data, I simply
> collected it."

This establishes (donor testimony): Simon is the observational/data-collection
donor; Bob Gray performed the historical processing and analysis; Simon does
not hold the search criteria or results. It does NOT establish any search
outcome.

## P0 — Search outcome (highest priority; gates everything quantitative)

1. Do any surviving analysis/search outputs exist (candidate lists, summary
   statistics, scan-through notes, working files) from the 1997–99
   processing — or from any later re-examination of the Hobart data?
2. Was any of the follow-up observing (1997–99, 2010, 2013/14) formally
   treated as a completed search with a recorded outcome?
3. Were any candidate events identified — including ones later rejected?

## P1 — Search selection (needed for any selection-function reconstruction)

4. What detection threshold / S/N criterion was used?
5. What constituted a "candidate" (in the SAS sigma-space diagnostics:
   what did COUNT·SIGMA_RD, TIME·CHANNEL·SIGMA_P, MAX_SIG·CHANNEL
   diagnostics feed into)?
6. What RFI rejection / flagging rules were applied (including the meaning
   of any `Row_Flagged` field)?
7. Were candidates manually inspected before rejection/acceptance?
8. Was a repeat/persistence detection required for anything to count?
9. Were any time intervals, channels, or sessions excluded a priori?

## P2 — Historical processing (1998/99 software archaeology dependency)

10. Which version of the processing software was used, and does that version
    (or its missing subroutines/libraries) survive?
11. Can the missing subroutines/libraries of the supplied high-level Fortran
    program be recovered (e.g., lag→channel conversion, windowing,
    normalization routines)?
12. Are historical output files, scripts, or command histories available?

## P3 — Documentation

13. Are there reports, notebooks, plots beyond the four surviving `.gsf.gz`
    diagnostics, candidate tables, correspondence, or manuscript drafts
    documenting the searches?
14. Is there a formal statement of the search results (published or
    unpublished) covering the 2010 and 2013/14 campaigns?

## What "nothing survives" is worth

An explicit statement that the analysis layer is lost is itself a
scientifically useful result: it converts several gap-register items from
OPEN to CLOSED-AS-UNRECOVERABLE and makes the non-identifiability conclusion
defensible.

## Do not re-ask (already established from archive / Simon response)

- Session dates, pointings, and the field1/field2 East/West beam-locale
  design (GAP-HOB-002/003 resolved; donor-supported).
- The 2010 pointing geometry and calibration chain (GAP-HOB-004 geometry;
  2010 calibration VERIFIED).
- Measured 1-D beam FWHM 33.8′–36.8′ (GAP-HOB-015 partial).
- Dump cadence 5.0 s and donor-supported ~5 s record timing (GAP-HOB-014).
- Donor-side surviving-material completeness (Simon: "This is all there is…").
- The 1998–99 `.fit.gz` files are 1024-lag ACF products (established by
  inspection); we do not need Bob to re-describe the file format — only the
  transformations applied to them.

## Mapping to gap register

| Requirement | GAP-HOB items potentially affected |
|---|---|
| P0 | 009 (outcomes), 001 (completeness, donor-held scope) |
| P1 | 005 (thresholds), 006 (candidate rules), 007 (RFI), 008 (repeat) |
| P2 | 012 (1998/99 processing chain), 018 (channel-count discrepancy cause) |
| P3 | 009, 017 (campaign-to-publication relationship) |
