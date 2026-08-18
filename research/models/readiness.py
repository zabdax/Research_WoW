"""Evidence-readiness reports for H1/H3/H4 without invented population priors."""
from __future__ import annotations


MECHANISM_REGISTRY = {
    "H1": {
        "status": "blocked",
        "mechanisms": ["receiver or electronics artifact", "intermodulation", "terrestrial transmitter", "satellite/aircraft/radar", "atmospheric propagation", "recording or processing artifact"],
        "required_inputs": ["Big Ear receiver chain", "dual-horn combination behavior", "1977 spectrum allocation/transmitter environment", "archival raw records or engineering logs"],
    },
    "H4": {
        "status": "blocked",
        "mechanisms": ["directed power beam", "sidelobe leakage", "sweeping beacon"],
        "available_engineering": ["EIRP", "aperture", "frequency", "beam divergence", "duty-cycle ranges"],
        "required_inputs": ["transmitter-population prior", "distance distribution", "alignment/sweep geometry", "occurrence rate", "repeat/intercept process"],
    },
}


def h4_flux_density_jy(eirp_w: float, distance_m: float, bandwidth_hz: float) -> float:
    """Isotropic-equivalent spectral flux density; engineering relation only."""
    if min(eirp_w, distance_m, bandwidth_hz) <= 0:
        raise ValueError("EIRP, distance, and bandwidth must be positive.")
    return eirp_w / (4.0 * 3.141592653589793 * distance_m**2 * bandwidth_hz) / 1e-26


def h4_beamwidth_rad(wavelength_m: float, aperture_diameter_m: float) -> float:
    if min(wavelength_m, aperture_diameter_m) <= 0:
        raise ValueError("Wavelength and diameter must be positive.")
    return wavelength_m / aperture_diameter_m
