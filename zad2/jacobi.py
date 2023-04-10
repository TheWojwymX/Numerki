from typing import Type

import numpy as np

from zad2 import menu


# http://www.algorytm.org/procedury-numeryczne/metoda-jacobiego.html
# https://icis.pcz.pl/~rperlinski/strona/files/mn/lab08pom.pdf

def matrix_diagonal_nonzero(initial_matrix: np.array) -> np.array:
    matrix_size = initial_matrix.shape[0]
    while np.count_nonzero(np.diagonal(initial_matrix)) < matrix_size:
        for iterator in range(matrix_size):
            if initial_matrix[iterator, iterator] == 0:
                initial_matrix[[iterator, iterator + 1]] = initial_matrix[[iterator + 1, iterator]]
    return initial_matrix

# def matrix_norm(matrix_m: np.array) -> Type[Exception] | None:
#     matrix_size = matrix_m.shape[0]
#     matrix_m_abs = np.abs(matrix_m)
#     matrix_m_sqr = np.square(matrix_m)
#     if (np.sum(matrix_m_abs.sum(axis=0)) >= matrix_size) and (
#             np.sum(matrix_m_abs.sum(axis=1)) >= matrix_size and (np.sqrt(np.sum(matrix_m_sqr) >= 1))):
#         return Exception
#     else:
#         return None

def is_convergent(matrix: np.array) -> bool:
    diag = np.abs(matrix.diagonal())
    off_diag = np.abs(matrix).sum(axis=1) - diag
    if np.all(diag > off_diag):
        return True
    else:
        raise Exception

# def l_d_u_matrix_creation(initial_matrix: np.array) -> tuple(np,):

def jacobi_method_iterations(initial_matrix: np.array, iterations: int) -> Type[Exception] | np.array:
    initial_matrix = matrix_diagonal_nonzero(initial_matrix)
    print(initial_matrix)
    initial_matrix_trimmed = initial_matrix
    initial_matrix_trimmed = np.delete(initial_matrix_trimmed, -1, 1)
    print(initial_matrix_trimmed)
    try:
        is_convergent(initial_matrix_trimmed)
        print("Matrix is convergent for Jacobi iterative method.")
    except:
        raise Exception("Matrix is not convergent for Jacobi iterative method.")
    matrix_size = initial_matrix.shape[0]

    matrix_l = initial_matrix
    matrix_l = np.delete(matrix_l, -1, 1)
    np.fill_diagonal(matrix_l, 0)
    matrix_l = np.tril(matrix_l)

    matrix_d = np.zeros((matrix_size, matrix_size))
    np.fill_diagonal(matrix_d, initial_matrix.diagonal())

    matrix_u = initial_matrix
    matrix_u = np.delete(matrix_u, -1, 1)
    np.fill_diagonal(matrix_u, 0)
    matrix_u = np.triu(matrix_u)

    matrix_n = np.zeros((matrix_size, matrix_size))
    for column_iterator in range(matrix_size):
        for row_iterator in range(matrix_size):
            if matrix_d[row_iterator, column_iterator] != 0:
                matrix_n[row_iterator, column_iterator] = np.reciprocal(matrix_d[row_iterator, column_iterator])
            else:
                matrix_n[row_iterator, column_iterator] = 0

    matrix_m = np.matmul(-matrix_n, (matrix_l + matrix_u))

    initial_vector = np.zeros(matrix_size)
    b_vector = initial_matrix[:, -1]

    vector = np.matmul(matrix_m, initial_vector) + np.matmul(matrix_n, b_vector)

    for iteration in range(1, iterations):
        vector = np.matmul(matrix_m, vector) + np.matmul(matrix_n, b_vector)

    return vector


try:
    menu.print_solutions_vector(
        jacobi_method_iterations(initial_matrix=menu.load_matrix_from_file("data_a.txt"), iterations=11))
except Exception as e:
    print(e)
# menu.print_solutions_vector(jacobi_method_iterations(initial_matrix=menu.load_matrix_from_file("data_b.txt"), iterations=11))
# menu.print_solutions_vector(jacobi_method_iterations(initial_matrix=menu.load_matrix_from_file("data_c.txt"), iterations=11))
menu.print_solutions_vector(jacobi_method_iterations(initial_matrix=menu.load_matrix_from_file("data_d.txt"), iterations=11))
# menu.print_solutions_vector(jacobi_method_iterations(initial_matrix=menu.load_matrix_from_file("data_e.txt"), iterations=11))
# menu.print_solutions_vector(jacobi_method_iterations(initial_matrix=menu.load_matrix_from_file("data_f.txt"), iterations=11))
menu.print_solutions_vector(jacobi_method_iterations(initial_matrix=menu.load_matrix_from_file("data_g.txt"), iterations=11))
# menu.print_solutions_vector(jacobi_method_iterations(initial_matrix=menu.load_matrix_from_file("data_h.txt"), iterations=11))
# menu.print_solutions_vector(jacobi_method_iterations(initial_matrix=menu.load_matrix_from_file("data_i.txt"), iterations=11))
menu.print_solutions_vector(jacobi_method_iterations(initial_matrix=menu.load_matrix_from_file("data_j.txt"), iterations=11))
