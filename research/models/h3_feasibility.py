"""H3 flux and brightness feasibility constraints, not an H3 occurrence likelihood."""
from __future__ import annotations

from dataclasses import dataclass
import math

SPEED_OF_LIGHT_M_S = 299_792_458.0
BOLTZMANN_J_K = 1.380_649e-23
JY_SI = 1e-26
KPC_M = 3.085_677_581_491_367e19


@dataclass(frozen=True)
class H3ReferenceConfiguration:
    reference_flux_jy: float = 1e-3
    reference_distance_kpc: float = 0.4
    observed_flux_lower_bound_jy: float = 250.0
    distance_min_kpc: float = 2.0
    distance_max_kpc: float = 4.9


def inverse_square_flux(reference_flux_jy: float, reference_distance_kpc: float, target_distance_kpc: float) -> float:
    if min(reference_flux_jy, reference_distance_kpc, target_distance_kpc) <= 0:
        raise ValueError("Flux and distances must be positive.")
    return reference_flux_jy * (reference_distance_kpc / target_distance_kpc) ** 2


def required_intrinsic_enhancement(configuration: H3ReferenceConfiguration, target_distance_kpc: float) -> float:
    return configuration.observed_flux_lower_bound_jy / inverse_square_flux(
        configuration.reference_flux_jy, configuration.reference_distance_kpc, target_distance_kpc
    )


def required_brightness_temperature_k(flux_jy: float, frequency_hz: float, solid_angle_sr: float) -> float:
    if min(flux_jy, frequency_hz, solid_angle_sr) <= 0:
        raise ValueError("Flux, frequency, and solid angle must be positive.")
    wavelength = SPEED_OF_LIGHT_M_S / frequency_hz
    return flux_jy * JY_SI * wavelength**2 / (2.0 * BOLTZMANN_J_K * solid_angle_sr)


def circular_source_solid_angle_sr(diameter_m: float, distance_kpc: float) -> float:
    if min(diameter_m, distance_kpc) <= 0:
        raise ValueError("Diameter and distance must be positive.")
    angular_diameter = diameter_m / (distance_kpc * KPC_M)
    return math.pi * (angular_diameter / 2.0) ** 2


def feasibility_summary(configuration: H3ReferenceConfiguration) -> dict[str, float]:
    return {
        "reference_to_observed_flux_ratio_at_reference_distance": configuration.observed_flux_lower_bound_jy / configuration.reference_flux_jy,
        "distance_min_predicted_flux_jy": inverse_square_flux(configuration.reference_flux_jy, configuration.reference_distance_kpc, configuration.distance_min_kpc),
        "distance_max_predicted_flux_jy": inverse_square_flux(configuration.reference_flux_jy, configuration.reference_distance_kpc, configuration.distance_max_kpc),
        "distance_min_required_enhancement": required_intrinsic_enhancement(configuration, configuration.distance_min_kpc),
        "distance_max_required_enhancement": required_intrinsic_enhancement(configuration, configuration.distance_max_kpc),
    }


def h3_readiness() -> dict[str, object]:
    return {
        "status": "blocked",
        "reason": "Flux feasibility is quantified, but trigger fluence, cloud population/geometry priors, and event-rate distribution are not source-backed.",
        "prohibited": ["legacy p_flux", "H5 repeat-rate transfer", "five-way evidence"],
    }
