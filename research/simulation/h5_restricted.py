"""Restricted, auditable Monte Carlo check of the Kipping--Gray event definition.

This module intentionally reports a *restricted implementation comparison*, not
an exact reproduction claim. It uses parsed upstream observing dates and an
explicit Poisson top-hat model, then records binomial Monte Carlo uncertainty.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from typing import Iterable

import numpy as np

from research.simulation.h5_assets import parse_fortran_days


@dataclass(frozen=True)
class RestrictedH5Config:
    duration_seconds: float = 659.0
    lambda_per_day: float = 0.121
    beam_window_seconds: float = 72.0
    horn_gap_seconds: float = 162.0
    baseline_days: float = 2673.0
    followup_hours: float = 192.0
    realisations_per_seed: int = 10_000
    seeds: tuple[int, ...] = (1977, 2022, 4242, 8675309)


def _one_realisation(rng: np.random.Generator, config: RestrictedH5Config, days: np.ndarray) -> bool:
    duration_days = config.duration_seconds / 86400.0
    window_days = config.beam_window_seconds / 86400.0
    horn_gap_days = config.horn_gap_seconds / 86400.0
    # Starts before the first observing day can cover the first window.
    start = -duration_days
    n_events = rng.poisson(config.lambda_per_day * (config.baseline_days + duration_days))
    starts = rng.uniform(start, config.baseline_days, n_events)
    hits = 0
    for centre in np.concatenate((days, days + horn_gap_days)):
        covered = np.any((starts <= centre - window_days / 2) & (starts + duration_days >= centre + window_days / 2))
        hits += int(covered)
        if hits > 1:
            return False
    return hits == 1


def run_restricted_check(config: RestrictedH5Config = RestrictedH5Config()) -> dict[str, object]:
    if config.duration_seconds < config.beam_window_seconds:
        raise ValueError("Signal duration must cover the beam window.")
    days = np.asarray(parse_fortran_days())
    estimates = []
    for seed in config.seeds:
        rng = np.random.default_rng(seed)
        hits = sum(_one_realisation(rng, config, days) for _ in range(config.realisations_per_seed))
        p = hits / config.realisations_per_seed
        estimates.append({"seed": seed, "hits": hits, "realisations": config.realisations_per_seed, "big_ear_probability": p, "binomial_se": math.sqrt(p * (1 - p) / config.realisations_per_seed)})
    probabilities = np.asarray([item["big_ear_probability"] for item in estimates])
    pooled_p = float(probabilities.mean())
    penalty = math.exp(-config.lambda_per_day * config.followup_hours / 24.0)
    return {
        "interpretation": "Restricted Monte Carlo check only; equivalence to the published likelihood emulator is unresolved.",
        "config": asdict(config),
        "upstream_dates": {"count": len(days), "first": float(days[0]), "last": float(days[-1])},
        "per_seed": estimates,
        "big_ear_probability_mean": pooled_p,
        "between_seed_sd": float(probabilities.std(ddof=1)),
        "followup_poisson_penalty": penalty,
        "restricted_post_followup_estimate": pooled_p * penalty,
        "published_post_followup_map": 0.0178,
        "absolute_difference_from_published": pooled_p * penalty - 0.0178,
        "status": "comparison_only; no exact-reproduction claim",
    }
