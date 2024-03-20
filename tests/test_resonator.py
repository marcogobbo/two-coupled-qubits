"""
Test Resonator class.
"""

import pytest
from qutip import Qobj

from two_coupled_qubits import Resonator


@pytest.fixture(name="resonator")
def fixture_resonator() -> Qobj:
    """Resonator object."""
    return Resonator(n=5, w=7.00, c_r=368.440)


def test_v_rms(resonator):
    "Test the voltage root mean square of the resonator."
    assert round(resonator.v_rms * 1e6, 2) == 1.0
