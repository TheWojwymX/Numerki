from typing import Type
import numpy as np


def load_matrix_from_file(filename: str) -> Type[Exception] | np.array:
    try:
        loaded_matrix = np.array(np.loadtxt(f"data\\{filename}"))
        print(f"Loaded matrix correctly from file {filename}!")
    except:
        raise Exception("Loaded wrong file!")
    return loaded_matrix


def print_solutions_vector(matrix_solutions):
    if matrix_solutions is Exception:
        print("CONVERGENCE REQUIREMENT NOT MET")
    else:
        print(f"Solutions vector for given matrix is equal to: \n{matrix_solutions}")
