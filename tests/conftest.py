from asyncio import constants
import numpy as np
import pytest


@pytest.fixture
def input_dictionary() -> dict:
    items = {"K": [1, 1, 0, 0, 0, 1],
        "I": [1, 0, 0, 2, 0, 0],
        "O": [0, 3, 0, 0, 1, 0],
        "H": [0, 0, 1, 0, 2, 0],
        "Cl": [0, 1, 1, 0, 0, 1]}
    return items


@pytest.fixture
def input_dictionary_incorrect() -> dict:
    items = {"K": [1, 1, 0, 0, 0, 1],
        "I": [1, 0, 0, 2, 0],
        "O": [0, 3, 0, 0, 1, 0],
        "H": [0, 0, 1, 0, 2, 0],
        "Cl": [0, 1, 1, 0, 0, 1]}
    return items


@pytest.fixture
def validation_matrix():
    mat = np.array([[1, 1, 0, 0, 0, 1],
        [1, 0, 0, 2, 0, 0],
        [0, 3, 0, 0, 1, 0],
        [0, 0, 1, 0, 2, 0],
        [0, 1, 1, 0, 0, 1]])
    return mat


@pytest.fixture
def correct_balance_vector():
    return np.array([[-6., -1., -6., 3., 3., 7.]]).astype(float)


@pytest.fixture
def inverted_matrix():
    M = np.array([[1, 1, 0, 0, 0, 1],
        [1, 0, 0, 2, 0, 0],
        [0, 3, 0, 0, 1, 0],
        [0, 0, 1, 0, 2, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1]])

    M_inv = np.linalg.inv(M)
    return M_inv

@pytest.fixture
def augmented_matrix():
    M = np.array([
        [2,0,1,3,4,5],
        [2,0,1,3,4,5][::-1],
        [9,0,1,3,4,5],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1]
        ])
    return M


@pytest.fixture
def augmented_matrix_nullity_1(validation_matrix):
    M = np.array([[0, 0, 0, 0, 0, 1]])
    M = np.concatenate(( validation_matrix, M ), axis=0)
    return M


@pytest.fixture
def augmented_matrix_nullity_2(validation_matrix):
    M = np.array([[0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])
    M = np.concatenate(( validation_matrix[:4, :], M ), axis=0)
    return M


@pytest.fixture
def chemical_equation():
    constituents = ["KI", "KClO3", "HCl", "I2", "H2O", "KCl"]
    equation = "KI + KClO3 + HCl = I2 + H2O + KCl"
    correct_output = "6 KI + KClO3 + 6 HCl = 3 I2 + 3 H2O + 7 KCl"
    atoms_amounts = {"K": [1, 1, 0, 0, 0, 1],
        "I": [1, 0, 0, 2, 0, 0],
        "O": [0, 3, 0, 0, 1, 0],
        "H": [0, 0, 1, 0, 2, 0],
        "Cl": [0, 1, 1, 0, 0, 1]}
    return {"input_equation": equation, "output_equation": correct_output,
    "constituents": constituents, "atoms_amounts": atoms_amounts}


@pytest.fixture
def chemical_equation_methane():
    constituents = ["CH4", "O2", "CO2", "H2O"]
    equation = "CH4 + O2 = CO2 + H2O"
    correct_output = "CH4 + 2 O2 = CO2 + 2 H2O"
    atoms_amounts = {"O": [0, 2, 2, 1],
        "C": [1, 0, 1, 0],
        "H": [4, 0, 0, 2]}
    return {"input_equation": equation, "output_equation": correct_output,
    "constituents": constituents, "atoms_amounts": atoms_amounts}


@pytest.fixture
def chemical_equation_primary_alcohol():
    constituents = ["CH3CH2OH", "O2", "CH3CHO", "H2O"]
    equation = "CH3CH2OH + O2 = CH3CHO + H2O"
    correct_output = "2 CH3CH2OH + O2 = 2 CH3CHO + 2 H2O"
    atoms_amounts = {"O": [1, 2, 1, 1],
        "C": [2, 0, 2, 0],
        "H": [6, 0, 4, 2]}
    return {"input_equation": equation, "output_equation": correct_output,
    "constituents": constituents, "atoms_amounts": atoms_amounts}


@pytest.fixture
def chemical_equation_iron_oxide():
    constituents = ["Fe2O3", "C", "Fe", "CO2"]
    equation = "Fe2O3 + C = Fe + CO2"
    correct_output = "2 Fe2O3 + 3 C = 4 Fe + 3 CO2"
    atoms_amounts = {"O": [3, 0, 0, 2],
        "Fe": [2, 0, 1, 0],
        "C": [0, 1, 0, 1]}
    return {"input_equation": equation, "output_equation": correct_output,
    "constituents": constituents, "atoms_amounts": atoms_amounts}

"Fe2O3 + C = Fe + CO2"