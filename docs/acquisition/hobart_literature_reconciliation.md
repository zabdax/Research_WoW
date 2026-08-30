# Hobart ↔ Published-Literature Reconciliation

Date: 2026-08-25 · Scope: MASTER DIRECTIVE §7 · Companion data file:
`research/data/ellingsen_coordinate_provenance.yaml`

## 1. Publication chain established for the Hobart follow-ups

| Paper | Bibliographic identity | Verification level |
|---|---|---|
| Gray & Ellingsen 2002, "A Search for Periodic Emissions at the Wow Locale", ApJ 578:967–971 | **DOI 10.1086/342646** (Crossref-verified 2026-08-25) | IDENTITY VERIFIED; CONTENT UNVERIFIED (local PDF `wow_published.pdf` has matching page-range metadata but all text is vectorized outlines; 28/37 streams decompress with zero readable text — OCR required) |
| R. H. Gray 1994, "A Search of the 'Wow' Locale for Intermittent Radio Signals", Icarus 112 | DOI 10.1006/icar.1994.1199 | cited for lineage; not held locally |
| Gray & Marvel 2001, "A VLA Search for the Ohio State 'Wow'", ApJ 546 | DOI 10.1086/318272 | cited for lineage; not held locally |
| Kipping & Gray restricted-model work | project context only (see §5) | handled by separate validation track |
| Méndez et al., Wow! II arXiv:2508.10657v1; Wow! I arXiv:2408.08513v2 | frozen locally | FROZEN + partially reproduced (Phase A/C) |

Retrieval notes: Semantic Scholar rate-limited (HTTP 429 ×2); Crossref
bibliographic lookup succeeded; abstracts were not retrieved from any source.
Nothing below relies on remembered content — unverified claims are marked.

## 2. Coordinate provenance table

| Coordinate | Frame/Epoch | Source | Original/Reconstructed | Uncertainty | Intended use | Suitable for beam weighting |
|---|---|---|---|---|---|---|
| Positive-horn locale | J2000 (paper-stated) | Arecibo II Table 4 | modern reconstruction of archival observation | ±3 s RA; ±20′ Dec | canonical reference | YES (as reference only) |
| Negative-horn locale | J2000 | Arecibo II Table 4 | modern reconstruction | ±3 s; ±20′ | canonical reference #2 | YES |
| Historical archival coordinate(s) | B1950-era conventions | Ehman-lineage values via frozen CSV rows | historical archival | Dec beam-limited ±20′ | history/traceability | NO (superseded by Table 4 for geometry) |
| Error-box definition used by Hobart campaigns | UNKNOWN | GAP-HOB-016 | — | — | — | NO (undefined) |
| Hobart field1/field2/2010 commands | J2000 (RPFITS card) | archive | original campaign values | commanded-exact | campaign targets | NO until GAP-HOB-002/003/004 resolved |
| 1999 grid A–D | B1950 DOCUMENTED (+derived J2000 images) | top-level README | original + derived transform | — | history | NO |

Classes kept separate per directive: historical archival · modern
reconstructed · campaign target · error-box definition · inferred. No
coordinate was adopted merely because it is commonly quoted; the canonical
references are the frozen paper values with locators.

## 3. Reconciliation findings (geometric)

1. Field1/field2 sit 5.8′ / 4.9′ from the two horn locales respectively
   (`hobart_pointing_reconciliation.md`), and equal the precessed images of
   the 1999 grid points to <2 s. Consistent with a coherent multi-campaign
   locale strategy; intent formally unresolved.
2. The 2010 ON position is ~30′ from the positive-horn locale — inside one
   measured beamwidth but well off-center; purpose unknown.
3. Nothing in the received literature metadata contradicts the archive's
   internal consistency (README ↔ logs ↔ headers ↔ SU tables).

## 4. Reported sensitivity / outcomes comparison

- **Cannot yet be performed**: G&E 2002 full text is unreadable locally
  (vectorized PDF; OCR pending), and no outcome statements exist in the
  archive for 2010–2014 (GAP-HOB-009 OPEN).
- Frozen modern comparators available for context (not substituted for Hobart
  quantities): SNR 30.1±0.4σ; flux ≥256±63 Jy (censored lower bound);
  duration ≥73.4±0.5 s (censored); RV heliocentric −84±1 km/s.
- Rule upheld: absence of detection records in the archive is NOT evidence of
  non-detection.

## 5. Relationship to the Kipping & Gray question

Unchanged from the forensic phase: reproducing the published K&G computational
result (Question A) is independent of reconstructing Hobart observational
constraints (Question B). This reconciliation contributes to Question B only;
no number here may feed Question A or any emulator target.

## 6. Open literature actions (for human gate)

1. OCR or obtain machine-readable text of G&E 2002 to extract reported
   positions/sensitivity/outcomes for the 1997–99 era (would PARTIALLY resolve
   GAP-HOB-009/017 for that era).
2. Optionally acquire Gray 1994 and Gray & Marvel 2001 for the same era's
   selection documentation.
3. Ask Simon whether any post-2002 analysis reports exist for 2010–2014
   (question set Priority 2).
