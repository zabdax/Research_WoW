# Revised Model Assumptions Register

## Non-negotiable rules

- A posterior probability must be conditional on a named model version and configuration.
- A physical feasibility calculation is not a population prior.
- A lower/upper observational bound remains censored data; it is not silently converted to a central value.
- Source frequency/bandwidth/flux/transit/follow-up terms are not multiplied unless the model states the relevant conditional dependence.
- Non-detection updates a model's temporal and observational selection model; it is not an origin-class penalty.
- An incomplete hypothesis is **blocked**, not assigned an arbitrary low likelihood.

## Present model readiness

The revised registry intentionally marks H1--H4 blocked and H5 in progress. This is a scientific safeguard. The comparison function accepts only externally supplied, non-negative marginal evidences and does not consume legacy heuristic scores.

---

## AMENDMENT 2026-08-23 — post-Phase-A evidence-base update (authorized)

Following the frozen Arecibo Wow! II extraction (`research/data/mendez_evidence_vector.yaml`, freeze manifest `mendez_evidence_freeze_manifest.yaml`) and Phase C partial reproduction, the following assumption-level updates apply. Nothing below weakens the non-negotiable rules.

### Superseded observational inputs (historical comparison in `research/data/historical_vs_arecibo_parameters.csv`)
- **SNR**: 30.5±0.5 was the Ehman-1998 *historical* value (carried through Wow! I §II); the modern reconstructed value is **30.1 ± 0.4** (Gaussian beam fit). Legacy provenance now resolved.
- **Flux**: the modern constraint is the censored bound **≥256 ± 63 Jy** (beam-centered-equivalent; Table 4 + §6 equations). The legacy "≥250 Jy" was abstract wording and is excluded as a source value. A rounding-policy sensitivity is documented (`rounding_sensitivity_note`): unrounded intermediates give ≥250.1 ± 56 Jy; neither value is privileged.
- **Duration**: ≥73.4 ± 0.5 s (censored beam-transit quantity) replaces the legacy point-encoded 72 s. The 72-second quarantine rule stands: no value here is an intrinsic source duration.
- **Frequency**: 1420.726 ± 0.005 MHz confirmed; locator upgraded from abstract to Table 4 + §7 equations; frame semantics documented (GSR-tracked 2nd-LO chain).
- **Datetime** (22:16:06 EST / 03:16:06 UTC), **velocities** (VHEL −84±1, VLSR −74±2 km/s), and **source size** (≤1.9 ± 0.1′) are new vector entries; velocity transformation methodology remains partially undocumented in the paper and must be established before independent use.
- **Positions**: Table 4 horn-labelled coordinates adopted; the printed positive-horn galactic latitude −17.85° is a **confirmed typographical error** (independently computed b = −18.82°); use the computed or author-confirmed value only.

### H2 status
H2 moves from `blocked` to `partially_unlocked` (see `configs/research_status.yaml`, `h2_partial_unlock_state`). Available: modern observational evidence, archival provenance, partial reproduction (frequency genuine; flux arithmetic-only). Still incomplete: Big Ear observation operator (no published 2-D beam map; squint rests on a private strip chart), topocentric/covariance ephemerides, physical emission model, campaign-specific selection functions. **No formal marginal likelihood for H2 exists yet.**

### Unchanged
- H1/H4 remain blocked; H5 in progress; `confirmatory_comparison_enabled: false`.
- Censored data are never central values; feasibility is never population probability; MAP is never marginal likelihood.
- The Ohio-SETI v0a `FLUX` array (54 Jy calibration) remains `LEGACY_SUPERSEDED`; its SNR arrays remain valid transcribed-archival data.
