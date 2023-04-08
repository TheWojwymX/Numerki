from typing import Type

import numpy as np


def load_matrix_from_file(filename: str) -> Type[Exception] | np.matrix:
    try:
        loaded_matrix = np.matrix(np.loadtxt(f"data\\{filename}.txt"))
        print(f"Loaded matrix correctly from file {filename}.txt!")
    except:
        return Exception
    return loaded_matrix


def jacobi_method_iterations(initial_matrix: np.matrix, iterations: int) -> Type[Exception] | np.matrix:
    matrix_size = initial_matrix.shape[0]
    # print(matrix_size)
    # print(matrix_size)

    while np.count_nonzero(np.diagonal(initial_matrix)) < matrix_size:
        for iterator in range(matrix_size):
            if initial_matrix[iterator,iterator]==0:
                initial_matrix[[iterator, iterator+1]] = initial_matrix[[iterator+1, iterator]]

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

    matrix_m_abs = np.abs(matrix_m)
    matrix_m_sqr = np.square(matrix_m)
    # print(matrix_m_abs)
    # print(matrix_m_sqr)
    if (np.sum(matrix_m_abs.sum(axis=0)) >= matrix_size) or (
            np.sum(matrix_m_abs.sum(axis=1)) >= matrix_size or (np.sum(matrix_m_sqr) >= 1)):
        return Exception

    # print(matrix_m)
    # print(np.sum(matrix_m_abs.sum(axis=0)))
    # print(matrix_m_abs.sum(axis=1))
    initial_vector = np.zeros(matrix_size)
    b_vector = initial_matrix[:, -1]

    vector = np.matmul(matrix_m, initial_vector) + np.matmul(matrix_n, b_vector)
    # print(f"Current iteration: {0}")
    # print("Current solutions vector")
    # print(vector[:, -1])
    for iteration in range(1, iterations):
        vector = np.matmul(matrix_m, vector) + np.matmul(matrix_n, b_vector)
        # print(f"Current iteration: {iteration}")
        # print("Current solutions vector")
        # print(vector[:, -1])
    # print(f"Matrix l:\n{matrix_l}")
    # print(f"Matrix d:\n{matrix_d}")
    # print(f"Matrix u:\n{matrix_u}")
    # print(f"Matrix n:\n{matrix_n}")
    # print(f"Matrix m:\n{matrix_m}")
    # print(vector[:, -1])
    #
    # print(b_vector)
    # print(vector[:, -1])

    return vector[:, -1]


def print_solutions_vector(matrix_solutions):
    if matrix_solutions is Exception:
        print("CONVERGENCE REQUIREMENT NOT MET")
    else:
        print(f"Solutions vector for given matrix is equal to: \n{matrix_solutions}")


#
# matrix_0_solutions = jacobi_method_iterations(iterations=11,
#                                               initial_matrix=np.matrix(
#                                                   '4 -1 -0.2 2 30; -1 5 0 -2 0; 0.2 1 10 -1 -10; 0 -2 -1 4 5'))
#
# print_solutions_vector(matrix_0_solutions)
#
# matrix_a_solutions = jacobi_method_iterations(iterations=11,
#                                               initial_matrix=np.matrix(
#                                                   '3 3 1 12; 2 5 7 33; 1 2 1 8'))
# print_solutions_vector(matrix_a_solutions)
#
# matrix_d_solutions = jacobi_method_iterations(iterations=11,
#                                               initial_matrix=np.matrix(
#                                                   '1 0.2 0.3 1.5; 0.1 1 -0.3 0.8; -0.1 -0.2 1 0.7'))
#
# print_solutions_vector(matrix_d_solutions)

print()

print_solutions_vector(jacobi_method_iterations(initial_matrix=load_matrix_from_file("data_a"), iterations=11))
print_solutions_vector(jacobi_method_iterations(initial_matrix=load_matrix_from_file("data_b"), iterations=11))
print_solutions_vector(jacobi_method_iterations(initial_matrix=load_matrix_from_file("data_c"), iterations=11))
print_solutions_vector(jacobi_method_iterations(initial_matrix=load_matrix_from_file("data_d"), iterations=11))
print_solutions_vector(jacobi_method_iterations(initial_matrix=load_matrix_from_file("data_e"), iterations=11))
print_solutions_vector(jacobi_method_iterations(initial_matrix=load_matrix_from_file("data_f"), iterations=11))
print_solutions_vector(jacobi_method_iterations(initial_matrix=load_matrix_from_file("data_g"), iterations=11))
print_solutions_vector(jacobi_method_iterations(initial_matrix=load_matrix_from_file("data_h"), iterations=11))
print_solutions_vector(jacobi_method_iterations(initial_matrix=load_matrix_from_file("data_i"), iterations=11))
print_solutions_vector(jacobi_method_iterations(initial_matrix=load_matrix_from_file("data_j"), iterations=11))
