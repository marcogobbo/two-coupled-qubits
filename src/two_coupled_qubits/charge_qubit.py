"""Charge qubit class."""

from dataclasses import dataclass

import numpy as np
from qutip import Qobj
from scipy.constants import e, h, physical_constants, pi


@dataclass
class ChargeQubit:
    """Charge qubit class.

    Build the charge qubit hamiltonian from given parameters.

    Args:
        e_c (float): capacitance energy of the charge qubit in GHz;
        e_j (float): Josephson energy of the charge qubit in GHz;
        levels (int): number of levels of the charge qubit;
        n_g (int): offset charge of the charge qubit.
    """

    e_c: float
    e_j: float
    levels: int
    n_g: int = 0

    @property
    def dim(self) -> int:
        """The dimension of the charge qubit Hilbert space."""
        return 2 * self.levels + 1

    @property
    def w(self) -> float:
        """The (2π * ) resonant frequency of the charge qubit in GHz."""
        return 2 * np.pi * (np.sqrt(8 * self.e_j * self.e_c) - self.e_c)

    @property
    def c_s(self) -> float:
        """Shunt capacitance of the charge qubit in fF."""
        return (e**2 / (2 * h * (self.e_c * 1e9))) * 1e15

    @property
    def i_c(self) -> float:
        """Critical current of the charge qubit in nA."""
        return (
            h * (self.e_j * 1e9) * 2 * pi / physical_constants["mag. flux quantum"][0]
        ) * 1e9

    @property
    def h(self) -> Qobj:
        """Hamiltonian of the charge qubit as Qobj."""
        return Qobj(
            (
                np.diag(
                    4 * self.e_c * np.arange(-self.levels, self.levels + 1) - self.n_g
                )
                ** 2
            )
            + 0.5
            * self.e_j
            * (
                np.diag(-np.ones(2 * self.levels), 1)
                + np.diag(-np.ones(2 * self.levels), -1)
            )
        )

    @property
    def number(self) -> tuple[Qobj, Qobj]:
        """Number operator of the charge qubit as Qobj.

        Returns:
            tuple[Qobj, Qobj]: number operator in the charge basis and in the energy basis.
        """
        _, eigenvectors = self.h.eigenstates()

        n = Qobj(np.diag(np.arange(-self.levels, self.levels + 1)))

        return (n, n.transform(eigenvectors))
