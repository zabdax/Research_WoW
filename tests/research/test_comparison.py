import pytest

from research.models.comparison import normalized_posteriors
from research.models.registry import ready_for_comparison


def test_five_way_posterior_normalizes_evidences():
    priors = {"H1": 0.2, "H2": 0.2, "H3": 0.2, "H4": 0.2, "H5": 0.2}
    evidences = {"H1": 1.0, "H2": 2.0, "H3": 3.0, "H4": 4.0, "H5": 5.0}
    posterior = normalized_posteriors(priors, evidences)
    assert sum(posterior.values()) == pytest.approx(1.0)
    assert posterior["H5"] > posterior["H1"]


def test_comparison_rejects_non_normalized_priors():
    with pytest.raises(ValueError, match="sum to one"):
        normalized_posteriors({"H1": 0.5}, {"H1": 1.0})


def test_revised_models_are_not_prematurely_comparable():
    assert not ready_for_comparison()

def test_censored_measurement_safeguard():
    from research.data.loader import load_wow_observation
    observation = load_wow_observation()
    assert observation.event.flux_density.kind == 'lower_bound', 'M-9: Flux must remain censored'
    assert observation.event.flux_density.value == 250.0

def test_strict_comparison_gate_rejects_immature_models():
    from research.models.comparison import strict_five_way_comparison, IncompleteModelError
    priors = {'H1': 0.2, 'H2': 0.2, 'H3': 0.2, 'H4': 0.2, 'H5': 0.2}
    evidences = {'H1': 1.0, 'H2': 2.0, 'H3': 3.0, 'H4': 4.0, 'H5': 5.0}
    with pytest.raises(IncompleteModelError):
        strict_five_way_comparison(priors, evidences)
