"""
Tests for the Bayesian engine (Module C).
"""

import pytest
from src.bayesian_engine import (
    compute_posteriors,
    lingam_posterior,
    bayes_factor,
    HYPOTHESIS_IDS,
    compute_shared_rarity_penalty
)

def test_lingam_posterior():
    """Test the Lingam master equation with known inputs."""
    # If xi = 1, posterior should equal prior
    assert abs(lingam_posterior(0.5, 1.0) - 0.5) < 1e-10
    
    # If prior = 0, posterior should be 0
    assert abs(lingam_posterior(0.0, 100.0) - 0.0) < 1e-10
    
    # If prior = 1, posterior should be 1 (for xi > 0)
    assert abs(lingam_posterior(1.0, 0.5) - 1.0) < 1e-10
    
    # Test a specific calculation: P(T|C)=0.1, xi=10 -> P=0.1*10/(1+0.1*9) = 1/1.9 = 0.5263...
    expected = 1.0 / 1.9
    assert abs(lingam_posterior(0.1, 10.0) - expected) < 1e-10

def test_bayes_factor():
    """Test Bayes factor computation."""
    assert abs(bayes_factor(0.5, 0.25) - 2.0) < 1e-10
    assert abs(bayes_factor(0.25, 0.5) - 0.5) < 1e-10
    assert bayes_factor(0.5, 0.0) == float('inf')

def test_benford_correction():
    """Test the shared rarity penalty."""
    penalty = compute_shared_rarity_penalty(total_followup_hours=192.0, lambda_map_per_day=0.121)
    
    # exp(-192 * 0.121 / 24) = exp(-0.968) = 0.3798
    expected = 0.3798419628513787
    
    assert abs(penalty["penalty_factor"] - expected) < 1e-6
    assert "H3" in penalty["applies_to"]
    assert "H4" in penalty["applies_to"]
    assert "H5" in penalty["applies_to"]
    assert "H1" in penalty["does_not_apply_to"]
    assert "H2" in penalty["does_not_apply_to"]

def test_compute_posteriors():
    """Test the full engine."""
    result = compute_posteriors()
    
    # Posteriors should sum to 1
    assert abs(sum(result.posteriors.values()) - 1.0) < 1e-10
    
    # H2 (comet) should be the lowest
    h2_rank = [i for i, (h, _) in enumerate(result.ranking) if h == "H2"][0]
    assert h2_rank == len(HYPOTHESIS_IDS) - 1
    
    # Bayes factors should be self-consistent
    for i, h_i in enumerate(HYPOTHESIS_IDS):
        for j, h_j in enumerate(HYPOTHESIS_IDS):
            if i >= j:
                continue
            bf1 = result.bayes_factors[f"{h_i}_vs_{h_j}"].value
            # We don't store the reverse directly, but we can compute it
            lik_j = result.likelihoods[h_j].likelihood
            lik_i = result.likelihoods[h_i].likelihood
            bf2 = bayes_factor(lik_j, lik_i)
            
            if bf1 > 0 and bf2 > 0:
                assert abs(bf1 * bf2 - 1.0) < 1e-10
