import numpy as np
import pytest

from balchem.transformations import get_augmented_matrix


def test_create_correct_augmented_matrix(augmented_matrix):
    augmented_matrix_output, _ = get_augmented_matrix(augmented_matrix[:3, :])
    assert np.array_equal(augmented_matrix, augmented_matrix_output)


def test_create_correct_augmented_matrix_nullity_1(validation_matrix, augmented_matrix_nullity_1):
    augmented_matrix_output, _ = get_augmented_matrix(validation_matrix)
    assert np.array_equal(augmented_matrix_nullity_1, augmented_matrix_output)


def test_create_correct_augmented_matrix_nullity_2(validation_matrix, augmented_matrix_nullity_2):
    augmented_matrix_output, _ = get_augmented_matrix(validation_matrix[:4, :])
    assert np.array_equal(augmented_matrix_nullity_2, augmented_matrix_output)

