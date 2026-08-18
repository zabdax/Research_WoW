"""
Shared fixtures for pytest.
"""

import os
from pathlib import Path
import pytest

@pytest.fixture
def data_dir():
    """Return the path to the data directory."""
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data"
    )
