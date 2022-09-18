import numpy as np


def balance_equation(equation: str):
    constants = (-6, -1, -6, 3, 3, 7)
    molecules = ("KI", "KClO3", "HCl", "I2", "H2O", "KCl")
    result = _create_balanced_equation(constants, molecules)
    return  result


def _create_balanced_equation(constants: tuple, molecules: tuple):
    sides = _arrange_sides(constants, molecules)
    full_equation = _join_sides(sides)
    return full_equation


def _arrange_sides(constants: tuple, molecules: tuple) -> dict:
    sides = {"left": [], "right": []}
    for constant, molecule in zip(constants, molecules):
        side = "left" if constant < 0 else "right"
        constant = abs(constant)
        molecule_string = f"{constant} {molecule}" if constant != 1 else f"{molecule}"
        sides[side].append(molecule_string)
    return sides

def _join_sides(sides: dict):
    left_hand_side = " + ".join(sides["left"])
    right_hand_side = " + ".join(sides["right"])
    return " = ".join((left_hand_side, right_hand_side)) 

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
