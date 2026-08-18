"""Small, testable building blocks for a future Big Ear response model.

These functions do not claim a calibrated Big Ear beam. Calibration inputs must
be added before they are used as an event likelihood.
"""

from __future__ import annotations

import math


def gaussian_power_response(offset_fwhm: float) -> float:
    """Return normalized Gaussian power response at an offset in FWHM units."""
    return math.exp(-4.0 * math.log(2.0) * offset_fwhm**2)


def censored_lower_bound_probability(predicted_flux_jy: float, lower_bound_jy: float) -> float:
    """Deterministic feasibility indicator, not a population likelihood.

    A probabilistic flux likelihood requires an uncertainty model supplied by a
    hypothesis-specific physical model.
    """
    if predicted_flux_jy < 0 or lower_bound_jy < 0:
        raise ValueError("Flux densities must be non-negative.")
    return 1.0 if predicted_flux_jy >= lower_bound_jy else 0.0
