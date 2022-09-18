import numpy as np
import pytest

from balchem.constituents import get_molecules, get_atom_counts


def test_get_molecules(chemical_equation: dict):
    equation = chemical_equation["input_equation"]
    result = get_molecules(equation)
    assert result == chemical_equation["constituents"]


def test_get_atoms(chemical_equation: dict):
    molecules = chemical_equation["input_equation"]
    result, _ = get_atom_counts(molecules)
    assert result == chemical_equation["atoms_amounts"]


def test_get_atoms_methane(chemical_equation_methane: dict):
    molecules = chemical_equation_methane["input_equation"]
    result, _ = get_atom_counts(molecules)
    assert result == chemical_equation_methane["atoms_amounts"]