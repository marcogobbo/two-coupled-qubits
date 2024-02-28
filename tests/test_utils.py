"""
Test utils functions.
"""

from two_coupled_qubits import (
    capacitance,
    capacitance_energy,
    critical_current,
    josephson_energy,
)


def test_capacitance():
    """
    Test capacitance function.
    """
    c = capacitance(0.23)
    assert round(c, 2) == 84.22


def test_critical_current():
    """
    Test critical current function.
    """
    i_c = critical_current(16.34)
    assert round(i_c, 2) == 32.9


def test_capacitance_energy():
    """
    Test capacitance energy function.
    """
    e_c = capacitance_energy(84.22)
    assert round(e_c, 2) == 0.23


def test_josephson_energy():
    """
    Test Josephson energy function.
    """
    e_j = josephson_energy(32.9)
    assert round(e_j, 2) == 16.34
