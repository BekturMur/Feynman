from setuptools import setup, find_packages

setup(
    name="feynman",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "sympy>=1.9",
        "matplotlib>=3.4.0",
        "networkx>=2.6.0",
        "jupyter>=1.0.0",
    ],
    author="Bektur Mur",
    author_email="your.email@example.com",
    description="Feynman Diagram Calculator for Condensed Matter Theory",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BekturMur/Feynman",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.8",
) 