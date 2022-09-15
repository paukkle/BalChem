import numpy as np
import pytest

from balchem.transformations import create_matrix


def test_matrix_created_correctly_from_dict(input_dictionary, validation_matrix):
    mat = create_matrix(input_dictionary)
    assert np.allclose(mat, validation_matrix)

