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
