"""
Tests for parameter loader.
"""

import pytest
from src.parameter_loader import load_parameters

def test_load_parameters():
    with pytest.warns(UserWarning):
        params = load_parameters()
    
    assert params.signal.frequency_mhz == 1420.726
    assert params.signal.peak_flux_lower_bound_jy == 250.0
    
    assert params.h5_params.initial_map_likelihood == 0.323
    assert params.h5_params.post_nondetection_map_likelihood == 0.0178
    
    assert params.h4_params.eirp_threshold_w == 1e17
    
    # Verify unverified warnings are present
    assert len(params.unverified_fields) > 0
