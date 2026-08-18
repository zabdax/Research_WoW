from research.data.loader import load_wow_observation


def test_wow_observation_preserves_censored_constraints():
    observation = load_wow_observation()
    assert observation.event.frequency.value == 1_420_726_000.0
    assert observation.event.flux_density.kind == "lower_bound"
    assert observation.event.bandwidth.kind == "upper_bound"
    assert len(observation.event.sky_candidates) == 2
    assert len(observation.event.followup) == 2


def test_beam_duration_is_not_declared_intrinsic_duration():
    observation = load_wow_observation()
    assert "not automatically intrinsic" in observation.event.beam_crossing_duration.provenance.notes
