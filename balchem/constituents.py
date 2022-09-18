import string 

import numpy as np


def get_atom_counts(unbalanced_equation):
    molecules = get_molecules(unbalanced_equation)
    atom_counts, individual_atoms = _get_atom_counts_in_molecules(molecules)
    atoms_in_rows = {atom: [0] * len(molecules) for atom in individual_atoms}
    for molecule, atoms in atom_counts.items():
        idx = molecules.index(molecule)
        for atom, count in atoms.items():
            atoms_in_rows[atom][idx] = count
    return atoms_in_rows


def get_molecules(unbalanced_equation: str):
    to_be_replaced = "=+"
    for char in to_be_replaced:
        unbalanced_equation = unbalanced_equation.replace(char, " ")
    return unbalanced_equation.split()


def _get_atom_counts_in_molecules(molecules: list):
    atoms_in_molecules = {}
    individual_atoms = set()
    for molecule in molecules:
        atoms = {}
        temp_str = ""
        for char in molecule:
            if len(temp_str) == 0:
                temp_str += char
            elif char in (string.ascii_uppercase):
                _add_atom_counts(atoms, temp_str)
                temp_str = char
            else:
                temp_str += char
        if len(temp_str) > 0:
            _add_atom_counts(atoms, temp_str)
        atoms_in_molecules[molecule] = atoms
        individual_atoms.update(atoms.keys())

    return atoms_in_molecules, individual_atoms


def _add_atom_counts(atoms, temp_str):
    atom, amount = _count_atoms(temp_str)
    if atoms.get(atom) != None:
        atoms[atom] += amount
    else:
        atoms[atom] = amount


def _count_atoms(sub_molecule: str):
    i = len(sub_molecule) - 1
    while True:
        try:
            int(sub_molecule[i])
            i -= 1
        except:
            i += 1
            break

    try:
        count = int(sub_molecule[i:])
    except:
        count = 1
    atom = sub_molecule[:i]
    return atom, count






get_atom_counts("KI + KClO3 + HCl = I2 + H2O + KCl")