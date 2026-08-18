import pytest

from research.models.h3_feasibility import H3ReferenceConfiguration, circular_source_solid_angle_sr, feasibility_summary, inverse_square_flux, required_brightness_temperature_k


def test_distance_scaling_and_required_enhancement_expose_flux_gap():
    config = H3ReferenceConfiguration()
    assert inverse_square_flux(1e-3, 0.4, 0.4) == pytest.approx(1e-3)
    summary = feasibility_summary(config)
    assert summary["reference_to_observed_flux_ratio_at_reference_distance"] == pytest.approx(250_000)
    assert summary["distance_min_required_enhancement"] > 1e6


def test_brightness_temperature_obeys_inverse_solid_angle_scaling():
    omega = circular_source_solid_angle_sr(1.2e5, 2.0)
    temperature = required_brightness_temperature_k(250.0, 1_420_726_000.0, omega)
    assert temperature > 0
    assert required_brightness_temperature_k(250.0, 1_420_726_000.0, omega / 2) == pytest.approx(temperature * 2)
