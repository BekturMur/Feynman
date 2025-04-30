import numpy as np
import matplotlib.pyplot as plt
from feynman import Diagram, MigdalVertex, GreenFunction
from feynman.utils import calculate_self_energy, migdal_approximation_valid

def test_migdal_approximation():
    """Test the validity of Migdal's approximation"""
    print("\nTesting Migdal's approximation validity:")
    # Test case 1: Valid case (small phonon frequency)
    is_valid = migdal_approximation_valid(phonon_frequency=0.1, fermi_energy=1.0, coupling_strength=0.5)
    print(f"Case 1 (valid): phonon_freq=0.1, fermi_energy=1.0, coupling=0.5 -> {is_valid}")
    
    # Test case 2: Invalid case (large phonon frequency)
    is_valid = migdal_approximation_valid(phonon_frequency=0.5, fermi_energy=1.0, coupling_strength=0.5)
    print(f"Case 2 (invalid): phonon_freq=0.5, fermi_energy=1.0, coupling=0.5 -> {is_valid}")

def test_green_functions():
    """Test Green's function calculations"""
    print("\nTesting Green's functions:")
    
    # Create electron and phonon Green's functions
    g_electron = GreenFunction(energy=1.0, damping=0.1, is_phonon=False)
    g_phonon = GreenFunction(energy=0.1, damping=0.01, is_phonon=True)
    
    # Calculate and plot density of states
    omega_range = (-2, 2)
    omegas, dos_electron = g_electron.density_of_states(omega_range)
    _, dos_phonon = g_phonon.density_of_states(omega_range)
    
    plt.figure(figsize=(10, 6))
    plt.plot(omegas, dos_electron, label='Electron DOS')
    plt.plot(omegas, dos_phonon, label='Phonon DOS')
    plt.xlabel('Energy')
    plt.ylabel('Density of States')
    plt.legend()
    plt.title('Density of States')
    plt.grid(True)
    plt.savefig('density_of_states.png')
    print("Density of states plot saved as 'density_of_states.png'")

def test_diagram_calculation():
    """Test Feynman diagram calculations"""
    print("\nTesting Feynman diagram calculations:")
    
    # Create vertices
    vertex1 = MigdalVertex(coupling_strength=0.5, phonon_frequency=0.1)
    vertex2 = MigdalVertex(coupling_strength=0.5, phonon_frequency=0.1)
    
    # Create diagram
    diagram = Diagram([vertex1, vertex2])
    print(f"Created diagram with {len(diagram.vertices)} vertices")
    
    # Visualize diagram
    diagram.plot(save_path='feynman_diagram.png')
    print("Feynman diagram plot saved as 'feynman_diagram.png'")
    
    # Calculate self-energy
    temperature = 0.01
    self_energy = calculate_self_energy(diagram, temperature)
    
    # Plot self-energy
    plt.figure(figsize=(10, 6))
    plt.plot(np.imag(self_energy), label='Imaginary part')
    plt.plot(np.real(self_energy), label='Real part')
    plt.xlabel('Matsubara frequency index')
    plt.ylabel('Self-energy')
    plt.legend()
    plt.title('Self-energy calculation')
    plt.grid(True)
    plt.savefig('self_energy.png')
    print("Self-energy plot saved as 'self_energy.png'")

if __name__ == "__main__":
    print("Starting Feynman Diagram Calculator tests...")
    test_migdal_approximation()
    test_green_functions()
    test_diagram_calculation()
    print("\nAll tests completed!") 