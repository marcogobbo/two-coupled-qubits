"""A collection of useful functions for common evaluations."""

from numpy import abs
from scipy.constants import e, h, pi

Phi_0 = h / (2 * e)


def find_idx(data, value):
    """Return the index of the array with the corresponding value."""
    return abs(data - value).argmin()


def capacitance(e_c):
    """Return the capacitance value in fF from the capacitance energy."""
    return (e**2 / (2 * h * (e_c * 1e9))) * 1e15


def critical_current(e_j):
    """Return the critical current value in nA from the Josephson energy."""
    return (h * (e_j * 1e9) * 2 * pi / Phi_0) * 1e9


def capacitance_energy(c):
    """Returm the capacitance energy value in GHz from the capacitance."""
    return (e**2 / (2 * h * (c * 1e-15))) * 1e-9


def josephson_energy(i_c):
    """Return the Josephson energy value in GHz from the critical current."""
    return ((i_c * 1e-9) * Phi_0 / (2 * pi * h)) * 1e-9
