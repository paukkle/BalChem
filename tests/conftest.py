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