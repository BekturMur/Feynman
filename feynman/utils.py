import numpy as np
import sympy as sp
from typing import List, Tuple, Optional
from .diagram import Diagram
from .vertex import MigdalVertex
from .green_function import GreenFunction

def visualize_diagram(diagram: Diagram, save_path: Optional[str] = None):
    """
    Visualize a Feynman diagram.
    
    Args:
        diagram: The diagram to visualize
        save_path: Optional path to save the figure
    """
    diagram.plot(save_path)

def calculate_self_energy(diagram: Diagram, 
                         temperature: float = 0.0,
                         n_matsubara: int = 100) -> np.ndarray:
    """
    Calculate the self-energy for a given diagram.
    
    Args:
        diagram: The diagram to calculate
        temperature: Temperature in energy units
        n_matsubara: Number of Matsubara frequencies to include
        
    Returns:
        Array of self-energy values at Matsubara frequencies
    """
    # This is a simplified implementation
    # A real implementation would involve proper integration over internal momenta
    omega_n = np.array([(2*n + 1) * np.pi * temperature for n in range(n_matsubara)])
    return -1j * np.sign(omega_n) * 0.1  # Simple approximation

def migdal_approximation_valid(phonon_frequency: float,
                             fermi_energy: float,
                             coupling_strength: float) -> bool:
    """
    Check if Migdal's approximation is valid for given parameters.
    
    Args:
        phonon_frequency: Characteristic phonon frequency
        fermi_energy: Fermi energy
        coupling_strength: Electron-phonon coupling strength
        
    Returns:
        True if Migdal's approximation is valid
    """
    return (phonon_frequency / fermi_energy) < 0.1 and coupling_strength < 1.0

def calculate_vertex_correction(vertex: MigdalVertex,
                              green_electron: GreenFunction,
                              green_phonon: GreenFunction,
                              temperature: float = 0.0) -> complex:
    """
    Calculate the vertex correction beyond Migdal's approximation.
    
    Args:
        vertex: The vertex to calculate correction for
        green_electron: Electron Green's function
        green_phonon: Phonon Green's function
        temperature: Temperature in energy units
        
    Returns:
        Complex value of the vertex correction
    """
    # This is a placeholder implementation
    # A real implementation would involve proper integration
    return 0.0 + 0.0j

def create_simple_diagram(n_vertices: int = 2) -> Diagram:
    """
    Create a simple diagram with specified number of vertices.
    
    Args:
        n_vertices: Number of vertices in the diagram
        
    Returns:
        A Diagram object
    """
    vertices = [MigdalVertex() for _ in range(n_vertices)]
    return Diagram(vertices) 