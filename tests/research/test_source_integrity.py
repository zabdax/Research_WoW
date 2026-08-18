from research.validation.source_integrity import audit_ledger


def test_source_ledger_assets_exist_and_marks_restrictions():
    report = audit_ledger()
    assert report["passed"]
    assert "mendez_2024" in report["restricted_as_sole_likelihood_support"]
    assert "naapo_rebuttal" in report["restricted_as_sole_likelihood_support"]
