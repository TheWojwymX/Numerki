import numpy as np

from zad2.jacobi import jacobi_method_iterations, jacobi_method_accuracy


def load_matrix_from_file(filename: str) -> np.array:
    try:
        loaded_matrix = np.array(np.loadtxt(f"data\\{filename}"))
        print(f"[INFO] Loaded matrix correctly from file {filename}!")
    except:
        raise Exception("[ERROR] Loaded wrong file!")
    return loaded_matrix


def run_all_files():
    for c in list(map(chr, range(ord('a'), ord('j') + 1))):
        print("\nIterations")
        try:
            result = jacobi_method_iterations(initial_matrix=load_matrix_from_file(f"data_{c}.txt"), iterations=7)
            print(f"Solutions vector for given matrix is equal to: \n{result[0]}")
            print(f"Achieved accuracy: {result[1]}")
        except Exception as e:
            print(e)
        print("\nAccuracy")
        try:
            result = jacobi_method_accuracy(initial_matrix=load_matrix_from_file(f"data_{c}.txt"), accuracy=0.0001)
            print(f"Solutions vector for given matrix is equal to: \n{result[0]}")
            print(f"Achieved after {result[1]} iterations")
        except Exception as e:
            print(e)

