"""Class for charge qubits."""

import matplotlib.pyplot as plt
import numpy as np
from qutip import Qobj


class ChargeQubit:
    """Define a charge qubit hamiltonian."""

    def __init__(self, e_c: float, e_j: float, levels: int, n_g: float):
        """Initialize the basic parameters for the hamiltonian."""
        self.e_c = e_c
        self.e_j = e_j
        self.levels = levels
        self.n_g = n_g

    @property
    def hamiltonian(self) -> Qobj:
        """Hamiltonian of the charge qubit as Qobj."""
        self.h = Qobj(
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
        return self.h

    def build(self, n_g: float) -> Qobj:
        """Build the hamiltonian of the charge qubit as Qobj."""
        self.h = Qobj(
            (
                np.diag(4 * self.e_c * np.arange(-self.levels, self.levels + 1) - n_g)
                ** 2
            )
            + 0.5
            * self.e_j
            * (
                np.diag(-np.ones(2 * self.levels), 1)
                + np.diag(-np.ones(2 * self.levels), -1)
            )
        )
        return self.h

    def get_energy_spectrum(self, n_gs: np.ndarray):
        """Return a plot of the energy spectrum."""
        energies = np.array([self.build(n_g).eigenenergies() for n_g in n_gs])

        for i in range(3):
            plt.plot(n_gs, energies[:, i], label=f"$E_{i}$")

        plt.title(f"$E_J/E_C={round(self.e_j/self.e_c,2)}$")
        plt.xlabel("$n_g$")
        plt.ylabel("$E_n$ [GHz]")
        plt.legend()
        plt.show()
