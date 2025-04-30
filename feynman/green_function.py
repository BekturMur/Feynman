import sympy as sp
import numpy as np
from typing import Tuple, Optional
from scipy.integrate import quad

class GreenFunction:
    """
    A class representing Green's functions in condensed matter theory.
    
    This class implements both electron and phonon Green's functions,
    with support for Matsubara frequencies and real frequencies.
    """
    
    def __init__(self,
                 energy: float = 0.0,
                 damping: float = 0.1,
                 temperature: float = 0.0,
                 is_phonon: bool = False):
        """
        Initialize a Green's function.
        
        Args:
            energy: Characteristic energy (Fermi energy for electrons, phonon frequency for phonons)
            damping: Damping parameter (inverse lifetime)
            temperature: Temperature in energy units
            is_phonon: Whether this is a phonon Green's function
        """
        self.energy = energy
        self.damping = damping
        self.temperature = temperature
        self.is_phonon = is_phonon
        
        # Create symbolic variables
        self.omega = sp.symbols('omega')
        self.k = sp.symbols('k_x k_y k_z')
        
    def matsubara(self, n: int) -> sp.Expr:
        """
        Calculate the Green's function at Matsubara frequency.
        
        Args:
            n: Matsubara frequency index
            
        Returns:
            A symbolic expression for the Green's function
        """
        omega_n = (2*n + 1) * np.pi * self.temperature if not self.is_phonon else 2*n * np.pi * self.temperature
        
        if self.is_phonon:
            return 1 / (omega_n**2 + self.energy**2)
        else:
            return 1 / (sp.I * omega_n - self.energy + sp.I * self.damping)
    
    def retarded(self, omega: float) -> complex:
        """
        Calculate the retarded Green's function at real frequency.
        
        Args:
            omega: Real frequency
            
        Returns:
            Complex value of the retarded Green's function
        """
        if self.is_phonon:
            return 1 / (omega**2 - self.energy**2 + 1j * omega * self.damping)
        else:
            return 1 / (omega - self.energy + 1j * self.damping)
    
    def spectral_function(self, omega: float) -> float:
        """
        Calculate the spectral function A(omega) = -Im G^R(omega)/pi.
        
        Args:
            omega: Real frequency
            
        Returns:
            Value of the spectral function
        """
        return -np.imag(self.retarded(omega)) / np.pi
    
    def density_of_states(self, omega_range: Tuple[float, float], n_points: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculate the density of states over a frequency range.
        
        Args:
            omega_range: Tuple of (omega_min, omega_max)
            n_points: Number of points to calculate
            
        Returns:
            Tuple of (frequencies, density_of_states)
        """
        omegas = np.linspace(omega_range[0], omega_range[1], n_points)
        dos = np.array([self.spectral_function(omega) for omega in omegas])
        return omegas, dos
    
    def __str__(self) -> str:
        return (f"GreenFunction(energy={self.energy}, "
                f"damping={self.damping}, "
                f"temperature={self.temperature}, "
                f"is_phonon={self.is_phonon})")
    
    def __repr__(self) -> str:
        return self.__str__() 