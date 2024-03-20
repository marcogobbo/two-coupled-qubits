"""
Test Charge Qubit class.
"""

import pytest
from qutip import Qobj

from two_coupled_qubits import ChargeQubit


@pytest.fixture(name="charge_qubit")
def fixture_charge_qubit() -> Qobj:
    """Charge Qubit object."""
    return ChargeQubit(e_c=0.23084, e_j=16.34, levels=3, n_g=0)


def test_w(charge_qubit):
    """Test the (2π * ) resonant frequency of the charge qubit."""
    assert round(charge_qubit.w, 2) == 33.06


def test_c_s(charge_qubit):
    """Test the shunt capacitance of the charge qubit."""
    assert round(charge_qubit.c_s, 2) == 83.91


def test_i_c(charge_qubit):
    """Test the critical current of the charge qubit."""
    assert round(charge_qubit.i_c, 2) == 32.90
