"""Five-way Bayesian normalization for supplied marginal evidences only."""

from __future__ import annotations

import math
from typing import Mapping


class IncompleteModelError(RuntimeError):
    """Raised when an analysis attempts to normalize non-evidence scores."""


def normalized_posteriors(
    priors: Mapping[str, float], evidences: Mapping[str, float]
) -> dict[str, float]:
    """Compute P(H_i|D) from normalized priors and non-negative marginal evidences."""
    if set(priors) != set(evidences):
        raise ValueError("Priors and evidences must name exactly the same hypotheses.")
    if any(value < 0 for value in priors.values()):
        raise ValueError("Priors must be non-negative.")
    if any(value < 0 or not math.isfinite(value) for value in evidences.values()):
        raise ValueError("Evidences must be finite and non-negative.")
    prior_total = sum(priors.values())
    if not math.isclose(prior_total, 1.0, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("Priors must sum to one before inference.")
    weights = {key: priors[key] * evidences[key] for key in priors}
    normalizer = sum(weights.values())
    if normalizer == 0:
        raise ValueError("At least one prior-weighted evidence must be positive.")
    return {key: value / normalizer for key, value in weights.items()}


def bayes_factor(evidence_i: float, evidence_j: float) -> float:
    if evidence_i < 0 or evidence_j < 0:
        raise ValueError("Evidences must be non-negative.")
    if evidence_j == 0:
        return math.inf if evidence_i > 0 else 1.0
    return evidence_i / evidence_j
