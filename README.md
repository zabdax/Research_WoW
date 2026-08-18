# Wow! Signal Bayesian Triage Research Program

This repository contains two deliberately separated workstreams for research on anomalous narrowband radio transients using the 1977 Wow! Signal as a case study.

- **Legacy Phase 2 prototype:** original exploratory source/data/code/manuscript artifacts at the repository root. It is preserved by Git tag `phase2-prototype-audit`. Its posterior-like outputs depend on hand-elicited component scores and are not confirmatory Bayesian evidences. See [`docs/legacy_status.md`](docs/legacy_status.md).
- **Revised research framework:** new, provenance-aware and model-conditional work in [`research/`](research/). It is designed to admit ambiguity and block a five-way ranking until every hypothesis has a defensible physical, observational, rate, and follow-up likelihood.

## Current research status

The project is in reconstruction, not attribution. No revised hypothesis ranking is currently produced. The next evidence gates are Big Ear geometry, a campaign-specific follow-up model, an independent restricted H5 replication, an adversarial H1 model, an H2 ephemeris reconstruction, and an H3 flux/rate feasibility analysis.

## Run the preserved baseline

```bash
py -m pytest
py -m scripts.legacy_report
```

This produces an audit report under `results/legacy/` without modifying the original `data/` result artifacts.

## Validate revised structured inputs

```bash
py -m research.validation.source_audit
```

## Principles

- Do not treat a normalized heuristic score as a Bayes factor or posterior evidence.
- Do not transfer Kipping & Gray's H5 event rate to another physical model.
- Do not discard the original work; preserve it, reproduce it, and compare it explicitly against the revised analysis.
- Do not present preprints as peer-reviewed confirmation.
- No result is a definitive attribution of the Wow! Signal.
