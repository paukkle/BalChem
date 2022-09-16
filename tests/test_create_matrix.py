from sqlite3 import DataError
import numpy as np
import pytest

from balchem.transformations import create_matrix


def test_matrix_created_correctly_from_dict(input_dictionary, validation_matrix):
    mat = create_matrix(input_dictionary)
    assert np.allclose(mat, validation_matrix)


def test_matrix_creation_fails_incorrect_input(input_dictionary_incorrect):
    with pytest.raises(ValueError):
        create_matrix(input_dictionary_incorrect)


def test_matrix_creation_fails_empty_rows():
    M = {"first": [], "second": []}
    with pytest.raises(ValueError):
        create_matrix(M)


def test_matrix_creation_fails_empty_dict():
    M = {}
    with pytest.raises(ValueError):
        create_matrix(M)