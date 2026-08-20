"""
H3 Population Prior: HI cloud catalog constraints and event-rate parameterization.

This module establishes the empirical basis for an H3 (Interstellar HI maser flare) prior.
It does NOT produce a direct event-rate prior, but structures the causal chain required 
to compute one when given appropriate density and trigger-rate estimations.

The causal chain is explicitly separated into four distinct factors:
1. HI Population (Observationally constrained by surveys like HI4PI)
2. Physical Conditions (Cold, dense, sufficiently large clouds capable of masing)
3. Triggering Mechanism (e.g., passing magnetars, highly model-dependent)
4. Maser Event Rate (Frequency of alignment and emission)
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping

@dataclass(frozen=True)
class HIDensityModel:
    """Empirical constraints on the foreground HI population."""
    catalog_source: str = "HI4PI (HI 4-PI Survey)"
    column_density_cm2_min: float = 1e20  # Minimum required for triggering (model assumption)
    average_ambient_temperature_k: float = 2.2  # Derived from non-detection bounds/DSR mechanics
    spatial_distribution: str = "galactic_plane_concentration"
    status: str = "observationally_constrained"


@dataclass(frozen=True)
class MaserTriggerMechanism:
    """The sequence of events bridging a passive cloud to a transient maser."""
    trigger_source: str = "Magnetar or Soft Gamma Repeater (SGR)"
    locus: str = "astrophysical_shockwave or intense radiative pulse"
    alignment_requirement: str = "Line-of-sight geometric alignment with Earth"
    status: str = "model_dependent"


class H3PopulationPriorBase:
    """
    Formal framework mapping the empirical catalog to the transient event rate.
    """
    def __init__(self, hi_model: HIDensityModel, mechanism: MaserTriggerMechanism):
        self.hi_model = hi_model
        self.mechanism = mechanism

    def causal_chain_documentation(self) -> Mapping[str, str]:
        """Explicitly distinguish observationally constrained layers from model-dependent assumptions."""
        return {
            "1_hi_population": f"Empirical foreground cloud count from {self.hi_model.catalog_source} (Observationally constrained).",
            "2_physical_conditions": f"Sub-population meeting size and T ~ {self.hi_model.average_ambient_temperature_k}K thresholds (Partially constrained).",
            "3_triggering_mechanism": f"Rate of {self.mechanism.trigger_source} interactions with target clouds (Highly model-dependent).",
            "4_maser_event_rate": f"Joint probability of interaction and {self.mechanism.alignment_requirement} (Highly model-dependent)."
        }

    def readiness_status(self) -> dict[str, str]:
        return {
            "status": "blocked",
            "reason": "HI4PI cloud distribution is well-constrained, but magnetar interaction rate and geometric alignment probability remain speculative. Cannot emit numerical H3 prior until mechanism probabilities are anchored."
        }
