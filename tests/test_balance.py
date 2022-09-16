import numpy as np
import pytest

from balchem.balance import get_balance_vectors


def test_correct_result(correct_balance_vector, inverted_matrix):
    balance_vectors = get_balance_vectors(inverted_matrix, 1)
    print(f"result: {balance_vectors}")
    print(f"test: {correct_balance_vector}")
    assert np.allclose(balance_vectors, correct_balance_vector)
