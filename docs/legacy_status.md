# Legacy Phase 2 Prototype Status

## Preservation status

The repository state tagged `phase2-prototype-audit` preserves the original Phase 2 prototype before the revised research architecture was added. The original top-level `src/`, `data/`, `figures/`, `logs/`, and `manuscripts/` artifacts remain in place and are not the revised inference engine.

## What the prototype does

- Normalizes five prior-weighted scalar values in `src/bayesian_engine.py`.
- Performs a one-at-a-time prior perturbation sweep in `src/sensitivity.py`.
- Checks portions of the Kipping & Gray (2022) follow-up algebra in `src/kg_validation.py` and includes an exploratory stochastic simulator.
- Records source metadata and verification labels in `data/parameters.yaml`.

## Interpretation boundary

The H1--H5 scalar values in the prototype include manually elicited component probabilities. They are not demonstrated marginal likelihoods of a joint generative physical-observation model. Consequently, legacy posterior values and Bayes factors are exploratory scoring outputs, not confirmatory scientific inferences.

The revised `research/` implementation must not reuse those component values as evidence. It may use the legacy pipeline only for historical reproduction and comparison.

## Known discrepancies and limitations

1. The current engine baseline does not reproduce the 75.3%, 16.5%, and 8.2% values stated in the manuscripts; the legacy report records the code output and the textual target separately.
2. The shared 192-hour Poisson scalar is derived from an H5 stochastic-repeater fit and is not a rate model for H3 or H4.
3. The prototype multiplies correlated factors without a demonstrated conditional-independence model.
4. The Level 1 Kipping--Gray gate validates algebraic consistency, not an independent full-likelihood reproduction.
5. The H3 >250 Jy flux requirement is not physically marginalized in the prototype.

## Legacy operation

Run `py -m scripts.legacy_report` to generate a new report under `results/legacy/`. This does not change historical result files under `data/`.
