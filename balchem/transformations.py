from sqlite3 import DataError
import numpy as np


def create_matrix(data: dict) -> np.array:
    def input_dimensions_ok(input_data: dict):
        lengths = [len(row) for _, row in input_data.items()]
        
        lengths_ok = len(set(lengths)) == 1 and lengths[0] > 0
        return lengths_ok

    if input_dimensions_ok(data):
        return np.array(list(data.values()))
    else:
        raise ValueError("Input row lengths are not equal to amount of columns.")


def get_augmented_matrix(matrix):
    nullity = _get_matrix_nullity(matrix)
    null_vectors = _get_null_vectors(matrix.shape[1], nullity)
    augmented_matrix = _augment_matrix(matrix, null_vectors)
    return augmented_matrix


def _augment_matrix(matrix: np.array, null_vectors: np.array):
    return np.concatenate((matrix, null_vectors), axis=0)


def _get_null_vectors(columns_amount: int, nullity: int):
    zero_columns = columns_amount - nullity
    return np.concatenate((np.zeros((nullity, zero_columns)), np.eye(nullity)), axis=1)


def _get_matrix_nullity(matrix: np.array):
    matrix_rank = _get_matrix_rank(matrix)
    return matrix.shape[1] - matrix_rank


def _get_matrix_rank(matrix: np.array):
    return np.linalg.matrix_rank(matrix)
