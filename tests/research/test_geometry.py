import pytest

from research.geometry.beam import censored_lower_bound_probability, gaussian_power_response


def test_gaussian_power_response_is_normalized_and_decreases():
    assert gaussian_power_response(0) == pytest.approx(1.0)
    assert gaussian_power_response(1) == pytest.approx(0.0625)


def test_flux_feasibility_respects_lower_bound():
    assert censored_lower_bound_probability(300, 250) == 1.0
    assert censored_lower_bound_probability(249, 250) == 0.0
