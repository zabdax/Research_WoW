from research.simulation.h5_restricted import RestrictedH5Config, run_restricted_check


def test_restricted_h5_reports_uncertainty_and_does_not_claim_equivalence():
    report = run_restricted_check(RestrictedH5Config(realisations_per_seed=100, seeds=(1, 2)))
    assert len(report["per_seed"]) == 2
    assert 0 <= report["restricted_post_followup_estimate"] <= 1
    assert "unresolved" in report["interpretation"]
