import numpy as np


def get_balance_vectors(inverted_matrix: np.array, nullity_number: int):
    null_space_vectors = _get_null_space_vectors(inverted_matrix, nullity_number)
    balance_arrays = _balance_vectors(null_space_vectors)
    return balance_arrays


def _get_null_space_vectors(matrix: np.array, nullity: int) -> np.array:
    return np.transpose(matrix[:, -nullity:])


def _balance_vectors(vectors: np.array):
    def find_nearest(array, number):
        diff_array = np.absolute(array - number)
        idx = diff_array.argmin()
        return abs(array[idx])

    for i in range(len(vectors)):
        vector = vectors[i, :]
        vectors[i, :] = (vector / find_nearest(vector, 0))

    return vectors
