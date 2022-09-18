import numpy as np
import pytest

from balchem.balance import get_balance_vectors, balance_equation


def test_correct_result_balance_vectors(correct_balance_vector, inverted_matrix):
    balance_vectors = get_balance_vectors(inverted_matrix, 1)
    assert np.allclose(balance_vectors, correct_balance_vector)


def test_balance_equation(chemical_equation: str):
    input_eq = chemical_equation["input_equation"]
    correct_output = chemical_equation["output_equation"]
    func_output = balance_equation(input_eq)
    assert correct_output == func_output


def test_balance_equation_methane(chemical_equation_methane: str):
    input_eq = chemical_equation_methane["input_equation"]
    correct_output = chemical_equation_methane["output_equation"]
    func_output = balance_equation(input_eq)
    assert correct_output == func_output


def test_balance_equation_primary_alcohol(chemical_equation_primary_alcohol: str):
    input_eq = chemical_equation_primary_alcohol["input_equation"]
    correct_output = chemical_equation_primary_alcohol["output_equation"]
    func_output = balance_equation(input_eq)
    assert correct_output == func_output


def test_balance_equation_iron_oxide(chemical_equation_iron_oxide: str):
    input_eq = chemical_equation_iron_oxide["input_equation"]
    correct_output = chemical_equation_iron_oxide["output_equation"]
    func_output = balance_equation(input_eq)
    assert correct_output == func_output