"""
Tests for the sensitivity analysis module.
"""

import pytest
from src.sensitivity import run_sensitivity_sweep
from src.bayesian_engine import HYPOTHESIS_IDS

def test_sensitivity_sweep():
    """Test that the sweep runs and produces valid bounds."""
    # Use small number of steps for fast testing
    results = run_sensitivity_sweep(steps=3)
    
    bounds = results["posterior_bounds"]
    
    # Check that bounds exist for all hypotheses
    for h_id in HYPOTHESIS_IDS:
        assert h_id in bounds
        assert bounds[h_id]["min"] >= 0.0
        assert bounds[h_id]["max"] <= 1.0
        assert bounds[h_id]["min"] <= bounds[h_id]["max"]
        
    # Check stability output
    stab = results["ranking_stability"]
    assert stab["total_sweeps"] == 15  # 5 hypotheses * 3 steps
    assert "baseline_top_rank" in stab
    assert isinstance(stab["is_stable"], bool)
