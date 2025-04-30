"""
Feynman Diagram Calculator for Condensed Matter Theory

This package provides tools for calculating Feynman diagrams in condensed matter theory,
with special focus on Migdal's theorem vertices and electron-phonon interactions.
"""

from .diagram import Diagram
from .vertex import MigdalVertex
from .green_function import GreenFunction
from .utils import visualize_diagram, calculate_self_energy

__version__ = "0.1.0"
__all__ = ['Diagram', 'MigdalVertex', 'GreenFunction', 'visualize_diagram', 'calculate_self_energy'] 