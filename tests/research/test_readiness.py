import pytest

from research.models.readiness import h4_beamwidth_rad, h4_flux_density_jy


def test_h4_engineering_calculations_are_deterministic_not_population_priors():
    assert h4_flux_density_jy(1e17, 3.085677581e19, 1e4) > 0
    assert h4_beamwidth_rad(0.21, 2190) == pytest.approx(0.21 / 2190)
