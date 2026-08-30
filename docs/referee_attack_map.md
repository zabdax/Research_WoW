# Referee Attack Map — Revised Research Program

| Claim area | Current evidence state | Principal objection | Required resolution before confirmatory comparison |
|---|---|---|---|
| Five-way Bayesian result | Legacy normalized score model | Inputs are not model evidences | Use only normalized marginal evidences from explicit generative models |
| H3 leading posterior | H3 includes elicited component values | 250 Jy feasibility, rate, and mechanism are not derived | Physical flux/brightness/rate model and posterior-predictive checks |
| H1 negligible | Qualitative factors | RFI competitor is a straw model | Adversarial RFI mixture with documented mechanism priors |
| H2 rejected | Inherited coordinate offset; [2026-08-23] Arecibo Wow! II revised coordinates, provenance-classified evidence vector, and partial reproduction (frequency genuine; flux arithmetic-only) now available — see Appendix A and frozen evidence vector | Coordinate frame, ephemeris, and beam response not independently reconstructed; full beam response still unpublished | Ephemeris/geometry likelihood with uncertainty; topocentric covariance-bearing ephemerides |
| H4 competitiveness | Engineering plausibility | Feasibility is not occurrence probability | Population, alignment, distance, duty-cycle and transmitter prior model |
| H5 reproduction | Level 1 algebra plus exploratory simulator | Algebra match is not likelihood equivalence | Locked restricted emulator, uncertainty, convergence and discrepancy report |
| Follow-up non-detection | Shared 192-hour scalar | Rate is model-specific; campaigns differ in selection | Campaign-specific detection efficiency and rate marginalization |
| Sensitivity claim | One-at-a-time perturbations | Does not explore the prior simplex or likelihood uncertainty | Dirichlet/scientific prior families and uncertainty propagation |
| Historical calibration | Six-row proof-of-concept census | Non-independent, hand-labelled, insufficient benchmark | Predeclared inclusion protocol and blind benchmark |
| Manuscript reproducibility | Draft prose contains manually typed output | Results drift from code | Generated tables/figures from frozen configurations only |
| Flux censoring (Arecibo II) | ≥256±63 Jy encoded as censored lower bound in frozen evidence vector; rounding sensitivity documented | "≥" paired with "±" has no formal statistical definition; bound is sensitive to intermediate rounding; calibration constants are paper-stated, not public-data-derived | Censored-data encoding + explicit rounding-sensitivity statement + constants treated as paper-stated inputs (see Appendix A) |

---

## APPENDIX A — Phase-A source-paper findings (2026-08-23)

### A.1 Table 4 galactic-coordinate typographical error — CONFIRMED by independent computation

**Finding.** In Arecibo Wow! II v1 (arXiv:2508.10657), Table 4 (`tab:wow`, frozen TeX l.436–440), the *new* positive-horn galactic latitude **b = −17.85° ± 0.04° is inconsistent with the same row's own J2000 coordinates** under the standard IAU transformation. Independent computation with astropy 7.2.2 `SkyCoord` (ICRS→Galactic), using only the paper's printed J2000 positions as inputs:

| Row | J2000 input (RA, Dec) | Computed (l, b) | Printed (l, b) | Δb |
|---|---|---|---|---|
| positive horn (new) | 19:25:02, −26:57:18 | 11.6175°, **−18.8181°** | 11.62°, −17.85° | **+0.968°** |
| positive horn (prev.) | 19:25:31, −26:57 | 11.6642°, −18.9165° | 11.65°, −18.89° | +0.027° |
| negative horn (new) | 19:27:55, −26:57:13 | 11.8672°, −19.4158° | 11.87°, −19.42° | +0.004° |
| negative horn (prev.) | 19:28:22, −26:57 | 11.9094°, −19.5079° | 11.90°, −19.48° | +0.028° |

Three of four rows validate to ≤0.03°; only the new positive-horn b fails, by ~1°. Inversion check: b = −17.85° at RA 19h25m02s would require Dec ≈ −28.00°, i.e. a 63′ declination shift contradicting the same row's tabulated −26:57:18. The computed value −18.82° agrees with the suspected intended −18.85° to within 0.03° (the row's own precision scale).

**Status:** `CONFIRMED_TYPO_INDEPENDENTLY_VERIFIED` (evidence vector `position_galactic`). The exact intended digits remain subject to author confirmation; the printed −17.85 must not be used downstream regardless. Reproduction: `research/validation/galactic_verification.py` → `research/data/processed/galactic_verification_results.json`.

### A.2 Flux rounding-sensitivity note (manuscript-ready text)

> The published flux constraint of Arecibo Wow! II, S_Wow = SNR_Wow × σ_channel ≥ 256 ± 63 Jy, is obtained through a chain of rounded intermediate quantities: σ_cnt = S_ntube/SNR_ntube = 9.4 Jy / (8.0 ± 1.8) → "1.2 ± 0.3 Jy"; σ_channel = σ_cnt·√50 → "8.5 ± 2.1 Jy"; and finally 30.1 × 8.5 → 256 Jy. Propagating the unrounded intermediates instead (σ_cnt = 1.175 Jy, σ_channel = 8.31 Jy) yields ≥250.1 ± 56 Jy, i.e. 2.3 % below the published bound. The divergence is caused entirely by the upward rounding of σ_cnt from 1.175 to 1.2 before multiplication by √50. We emphasize that this is a rounding-policy sensitivity in the published value, not a disagreement with the paper's method and not an arithmetic error on either side; neither value is privileged in our analysis. Because both are lower bounds on a beam-centered-equivalent flux whose true value is stated to be likely greater if the source was off-axis, all downstream uses treat the quantity as censored data rather than as a central measurement.

Cross-reference: censoring-semantics ambiguity (no formal definition of "≥" paired with "±"; beam-centered-equivalent caveat; ~2× under the alternative noise-tube calibrator) is documented in full prose in `research/data/mendez_evidence_vector.yaml` (`parameters.flux_density.censoring_semantics`) and reproduced arithmetically in `research/data/processed/mendez_reproduction_results.json` (`flux_arithmetic.unrounded_propagation_finding`).
