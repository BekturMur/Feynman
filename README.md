# Feynman Diagram Calculator for Condensed Matter Theory

A sophisticated Python package for calculating Feynman diagrams in condensed matter theory, with special focus on Migdal's theorem vertices and electron-phonon interactions.

## Features

- Calculation of Feynman diagrams up to arbitrary order
- Implementation of Migdal's theorem vertices
- Support for electron-phonon interactions
- Visualization of Feynman diagrams
- Numerical integration of diagrammatic expressions
- Symbolic manipulation of Green's functions

## Installation

```bash
git clone https://github.com/BekturMur/Feynman.git
cd Feynman
pip install -e .
```

## Dependencies

- Python 3.8+
- NumPy
- SciPy
- SymPy
- Matplotlib
- NetworkX
- Jupyter Notebook (for examples)

## Usage

```python
from feynman import Diagram, MigdalVertex, GreenFunction

# Create a basic electron-phonon vertex
vertex = MigdalVertex()
diagram = Diagram(vertex)

# Calculate the self-energy
self_energy = diagram.calculate_self_energy()

# Visualize the diagram
diagram.plot()
```

## Documentation

Detailed documentation is available in the `docs` directory.

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this software in your research, please cite:

```bibtex
@software{feynman_calculator,
  author = {Bektur Mur},
  title = {Feynman Diagram Calculator for Condensed Matter Theory},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/BekturMur/Feynman}
}
``` 