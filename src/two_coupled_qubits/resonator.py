"""Resonator class."""

from dataclasses import dataclass

import numpy as np
from qutip import Qobj, destroy
from scipy.constants import hbar


@dataclass
class Resonator:
    """Resonator class.

    Build the resonator hamiltonian from given parameters.

    Args:
        n (int): the dimension of the Fock space;
        w (float): the (2π * ) resonant frequency of the resonator in GHz;
        c_r (float): the capacity of the resonator in fF.
    """

    n: int
    w: float
    c_r: float

    @property
    def v_rms(self) -> float:
        """Voltage root mean square of the resonator in uV."""
        return np.sqrt((hbar * self.w * 1e9) / (2 * self.c_r * 1e-15))

    @property
    def h(self) -> Qobj:
        """Hamiltonian of the resonator."""
        a = destroy(self.n)
        return self.w * a.dag() * a
