# Hobart 1998/99 Evidence Baseline (Definitive)

Status: **consolidation of established evidence; NO inference performed** ·
Directive: POST-G&E/POST-SIMON consolidation, Part 1–2 ·
Sources: Gray & Ellingsen (2002) text extraction
(`research/data/ge2002_extraction.yaml`), frozen `.fit.gz` archive, MPSLPP
source/manual, Simon response freeze, gap register v1.3, prior forensic
reports.

## Evidence hierarchy (never collapsed)

| Class | Meaning |
|---|---|
| DIRECTLY_STATED | explicitly stated by Gray & Ellingsen (2002) |
| ARCHIVED | directly present in surviving source files |
| DONOR_SUPPORTED | explicitly stated by Simon Ellingsen |
| DERIVED | deterministically calculated from frozen source material |
| DOCUMENTATION_ONLY | described by software/manual documentation; not proven executed for the campaign |
| INFERRED | reasonable inference, not directly established |
| UNKNOWN / MISSING | not recoverable from current evidence |

## Guardian distinctions (invariant — guarded by tests)

```text
published non-detection != reconstructed selection function
raw archival data  != independently reproduced historical search
```

The Gray & Ellingsen (2002) result establishes a **published 1998/99
non-detection under the documented observational/search conditions**. It
does NOT by itself establish: P(no detection | H5); a Bayesian likelihood; a
detection efficiency; completeness for every signal class; completeness over
every flux/position/linewidth combination; a fully reconstructed historical
selection function; absence of candidate events prior to manual rejection;
or absence of all possible repeating signals.

## Q1 — What was observed?

Six ~14 hr **tracking** runs (not drift scans) on the two nominal Wow
locales and four ±15′ declination offset fields (DIRECTLY_STATED, Table 1).
Sessions correspond exactly to the archived `.fit.gz` products
w98278xx…w9910004 (ARCHIVED + DERIVED DOY match) and the 1999 README
session list (ARCHIVED).

## Q2 — Where?

Mount Pleasant Radio Observatory, University of Tasmania 26 m
(DIRECTLY_STATED, Table 2). Pointings: R.A. 19h22m22s / 19h25m12s (both
±5 s), Dec −27°03′ ± 20′ (B1950.0; Kraus 1990 private communication), plus
±15′ N/S coverage fields (DIRECTLY_STATED). Beam of origin ambiguous (Ohio
State recorded the unsigned difference of two beams 2m50s apart).

## Q3 — When?

1998 Oct 5 (DOY 278), 1998 Oct 9 (282); 1999 Mar 17–18 (76/77), Mar 20–21
(79/80), Mar 22–23 (81/82), Apr 9–10 (99/100) (DIRECTLY_STATED, Table 1).
Runs staggered over ~6 months so H i Doppler-shifts (DIRECTLY_STATED §3.1).
Archive incident corroboration: paper footnote "1 hr missing mid-run"
(1925S2) = README "lost concatenation 02–03 UT Mar 20/21" (ARCHIVED).

## Q4 — With what instrument?

UTAS 26 m; one-bit digital autocorrelation spectrometer; two linear
polarizations (crossed dipoles); HPBW 28′ at 21 cm (DIRECTLY_STATED,
Table 2). Data reduction used "a modified version of the observatory
spectral line analysis software (Ellingsen 1996)" — the published lineage of
MPSLPP (DIRECTLY_STATED); the executed software name/version is UNKNOWN.

## Q5 — Frequency / bandwidth / channel configuration?

Per-field centers 1420.3135–1420.5870 MHz (DIRECTLY_STATED, Table 1);
2.5 MHz total band; 4.88 kHz channel spacing; 9.765 kHz effective width
after Hanning; 512 channels per polarization (DIRECTLY_STATED, Table 2).
Archived products are 1024-lag ACFs per polarization (ARCHIVED);
1024 lags → 512 channels is CONSISTENT but the mapping is INFERRED
(paper does not state the lag count — UNKNOWN).

## Q6 — Integration time?

**30 s** per spectrum for 1998/99 (DIRECTLY_STATED, Table 2). (The
"≈5 s record" figure is DONOR_SUPPORTED for the **2013/14** dumps only —
different era, different correlator; never mixed.)

## Q7 — Calibration information available?

Noise diode vs total power every 10 minutes → Tsys = 1200 Jy (120 K);
absolute scale via Virgo A = 211 Jy at 1420 MHz (Baars et al. 1977);
σ = 2.46 Jy per 30 s spectrum, 0.55 Jy per reference (20 averaged),
quotient 2.5 Jy expected vs 2.6–3.0 Jy observed rms (DIRECTLY_STATED,
§2.1–2.2, Table 2). No calibration files survive in the archive (the
`.fit.gz` carry COUNTS-unit ACFs only) — the paper is the sole calibration
record (execution-level DOCUMENTATION_ONLY; publication-level
DIRECTLY_STATED).

## Q8 — What search procedure is explicitly published?

Quotient spectra Q = (S/R) − 1 with **self-references** formed by averaging
30 s on-source spectra between 10-minute calibrations; median-smoothing
(single-channel features) and iterative straight-line "bridging" (broader
features incl. H i and RFI); third-degree polynomial baseline on
emission/RFI-free regions; running baseline (nine prior measurements) for
buried signals; off-source RFI screening ~1 hr pre/post each run with
offending channels ignored; statistical threshold P_e = 0.05 (Thompson 1991)
plus manual feature inspection; default presumption that features are RFI
absent evidence otherwise (all DIRECTLY_STATED, §2.1–2.3, §3.1–3.3).

## Q9 — What thresholds are explicitly published?

Per-field 5.9σ; all-fields 6.2σ; signal thresholds 15.7–18.0 Jy (features
included) and 4.74–7.71 Jy (features excluded); per-field rms 2.66–3.0 Jy;
9,587,712 total samples (DIRECTLY_STATED + TABLE_VALUE, Table 3).

## Q10 — What was the published outcome?

**Published non-detection** (DIRECTLY_STATED):
- "No emissions resembling the Wow were detected over a bandwidth of 2.5 MHz
  to a flux density limit of about 18 Jy, with a detection threshold of
  5.9σ and rms noise of 3 Jy." (abstract)
- "Excluding these features as probable RFI, no spectral features remain
  that noticeably exceed the noise." (§3.3)
- "No signals resembling the Ohio State Wow were detected in observations
  dwelling for up to 14 hr at the coordinates where the signal was
  reported." (§4)

Two candidate features were described and rejected (1922N: 14σ
two-channel both-polarization single-integration feature +456 kHz from Wow;
1922N: 5.6σ at the Wow frequency, single integration, no
other-polarization counterpart — "too near the statistical noise peaks to
consider as a redetection"). Candidate catalogue status:
`PUBLISHED_RESULT_WITHOUT_SURVIVING_CANDIDATE_LEVEL_DATA`.

## Q11 — What temporal/repetition constraints were reported?

A source with period <14 hr would have been detected at least once;
nominal positions were covered twice → binomial detection probability
>0.90 for periods up to ~20 hr; single-run probability ≈14/t (t = period,
hours) for offset fields; longer periods and non-periodic emission are NOT
ruled out; probability of the original Ohio State detection <0.10 for
periods over ~12 hr (DIRECTLY_STATED §3.4/§4 + FIGURE_VALUE Fig. 3 caption;
curves not digitized).

## Q12 — Which candidate-level information survives?

Only the two described features (DIRECTLY_STATED). No complete candidate
list was published (NOT_STATED) and none survives in the donor-held archive
(NOT_FOUND_IN_SUPPLIED_ARCHIVE). The raw 122 `.fit.gz` ACF products survive
(ARCHIVED); whether every archived file was included in the published
search is not independently verifiable (UNKNOWN).

## Q13 — Which parts of the historical pipeline remain unreproducible?

All technical kernels (readfit, writefit, vanvleck, dofft, hanning, gausmoo,
gaufit, svdfit, …), all four INCLUDE files, CFITSIO/SLALIB/PGPLOT/menu
libraries (73/73 REFERENCED_BUT_MISSING — DEPENDENCY_MISSING); the executed
software version; the exact lag→channel mapping and window conventions; any
executed parameter deviations from the published description. No kernel has
been reconstructed (DOCUMENTATION_ONLY boundaries preserved).

## Q14 — Which conclusions ARE valid?

1. A published, peer-reviewed 1998/99 non-detection exists for the two
   B1950 Wow locales at the documented sensitivity (≈18 Jy, 5.9σ, 2.5 MHz).
2. The published period constraint (>14 hr; P>0.90 to ~20 hr at nominal
   positions) is a documented historical result.
3. The 1998/99 instrument configuration and per-field frequencies are
   documented and consistent with the archived ACF products and MPSLPP.
4. The paper, archive, and donor testimony are mutually consistent for
   1998/99 (no contradictions found; one era-level HPBW difference
   preserved).
5. The surviving raw ACF archive is complete donor-held material whose
   per-session center frequencies are now known.

## Q15 — Which conclusions must NOT be drawn?

1. Any P(no detection | H5), likelihood, Bayes factor, posterior, or
   detection efficiency from this record.
2. Search completeness over flux/position/linewidth/drift classes.
3. "No candidates existed" (two were described; catalogue absent).
4. "Every archived file was searched" (not independently verifiable).
5. Anything about the 2010/2013/14 campaigns (paper predates them).
6. That the historical ~60 Jy flux estimate or B1950 error box supersedes
   the frozen Arecibo II reconstruction (HISTORICAL DIFFERENCE, unresolved).
7. That the HPBW difference (28′ vs 33.8′–36.8′) indicates an error.
8. That data-product technical reproduction would equal scientific
   reproduction of the historical search.

---

## Appendix — Overinterpretation safeguards (directive Part 2)

The distinctions below are load-bearing and test-guarded
(`tests/research/test_consolidation_guards.py`):

1. `published non-detection != reconstructed selection function` — the
   paper's outcome is a historical claim under published conditions; the
   selection function requires executed-parameter recovery and is currently
   non-identifiable.
2. `raw archival data != independently reproduced historical search` —
   holding the `.fit.gz` files does not reproduce the search; kernels are
   missing and no re-execution has been attempted.
3. `absence of a surviving candidate list != absence of candidates`.
4. `qualitative donor statements != statistical uncertainties`
   (Simon's ≈50% is not σ=50%; his "5 s record" is not a measured
   integration for 2013/14).
5. `era separation` — 1998/99 (30 s, 512 ch, 2.5 MHz, one-bit ACF,
   MPSLPP-lineage) vs 2010/2013/14 (RPFITS, 4096-ch raw, 4/8/16 MHz,
   5 s cadence, newer correlator) are never mixed.



