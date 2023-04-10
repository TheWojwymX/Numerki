import numpy as np

from zad2 import menu


# http://www.algorytm.org/procedury-numeryczne/metoda-jacobiego.html
# https://icis.pcz.pl/~rperlinski/strona/files/mn/lab08pom.pdf

def ensure_that_matrix_diagonal_is_nonzero(initial_matrix: np.array) -> np.array:
    matrix_size = initial_matrix.shape[0]
    while np.count_nonzero(np.diagonal(initial_matrix)) < matrix_size:
        for iterator in range(matrix_size):
            if initial_matrix[iterator, iterator] == 0:
                initial_matrix[[iterator, iterator + 1]] = initial_matrix[[iterator + 1, iterator]]
    return initial_matrix


def is_convergent(matrix: np.array) -> bool:
    diag = np.abs(matrix.diagonal())
    off_diag = np.abs(matrix).sum(axis=1) - diag
    if np.all(diag > off_diag):
        return True
    else:
        raise Exception


def helper_matrix_creation(initial_matrix: np.array, initial_matrix_trimmed: np.array, matrix_size: int) \
        -> tuple[np.array, np.array, np.array]:
    matrix_l = initial_matrix_trimmed
    np.fill_diagonal(matrix_l, 0)
    matrix_l = np.tril(matrix_l)

    matrix_d = np.zeros((matrix_size, matrix_size))
    np.fill_diagonal(matrix_d, initial_matrix.diagonal())

    matrix_u = initial_matrix_trimmed
    np.fill_diagonal(matrix_u, 0)
    matrix_u = np.triu(matrix_u)

    return matrix_l, matrix_d, matrix_u


def matrix_n_creation(matrix_d: np.array, matrix_size: int) -> np.array:
    matrix_n = np.zeros((matrix_size, matrix_size))
    for column_iterator in range(matrix_size):
        for row_iterator in range(matrix_size):
            if matrix_d[row_iterator, column_iterator] != 0:
                matrix_n[row_iterator, column_iterator] = np.reciprocal(matrix_d[row_iterator, column_iterator])
            else:
                matrix_n[row_iterator, column_iterator] = 0

    return matrix_n


def jacobi_method_iterations(initial_matrix: np.array, iterations: int) -> tuple[np.array, np.float64]:
    initial_matrix = ensure_that_matrix_diagonal_is_nonzero(initial_matrix)
    initial_matrix_trimmed = np.delete(initial_matrix, -1, 1)
    try:
        is_convergent(initial_matrix_trimmed)
        print("Matrix is convergent for Jacobi iterative method.")
    except Exception:
        raise Exception("Matrix is not convergent for Jacobi iterative method.")

    matrix_size = initial_matrix.shape[0]

    matrix_l, matrix_d, matrix_u = helper_matrix_creation(initial_matrix, initial_matrix_trimmed, matrix_size)

    matrix_n = matrix_n_creation(matrix_d, matrix_size)

    matrix_m = np.matmul(-matrix_n, (matrix_l + matrix_u))

    initial_vector = np.zeros(matrix_size)
    b_vector = initial_matrix[:, -1]

    error_list = list()
    vector = np.matmul(matrix_m, initial_vector) + np.matmul(matrix_n, b_vector)

    for iteration in range(1, iterations):
        error_list = list()
        new_vector = np.matmul(matrix_m, vector) + np.matmul(matrix_n, b_vector)
        for index in range(new_vector.size):
            error = new_vector[index] - vector[index]
            error_list.append(error)
        vector = new_vector
    accuracy = str(max(error_list))
    return new_vector, np.power(10.0, (-int(accuracy[::-1].find('.')) + 1))


def jacobi_method_accuracy(initial_matrix: np.array, accuracy: float) -> tuple[np.array, int]:
    initial_matrix = ensure_that_matrix_diagonal_is_nonzero(initial_matrix)
    initial_matrix_trimmed = np.delete(initial_matrix, -1, 1)
    try:
        is_convergent(initial_matrix_trimmed)
        print("Matrix is convergent for Jacobi iterative method.")
    except Exception:
        raise Exception("Matrix is not convergent for Jacobi iterative method.")

    matrix_size = initial_matrix.shape[0]

    matrix_l, matrix_d, matrix_u = helper_matrix_creation(initial_matrix, initial_matrix_trimmed, matrix_size)

    matrix_n = matrix_n_creation(matrix_d, matrix_size)

    matrix_m = np.matmul(-matrix_n, (matrix_l + matrix_u))

    initial_vector = np.zeros(matrix_size)
    b_vector = initial_matrix[:, -1]

    vector = np.matmul(matrix_m, initial_vector) + np.matmul(matrix_n, b_vector)
    iterations = 1
    while True:
        error_list = list()
        is_finished = True
        new_vector = np.matmul(matrix_m, vector) + np.matmul(matrix_n, b_vector)
        for index in range(new_vector.size):
            error = new_vector[index] - vector[index]
            error_list.append(error)
        for error in error_list:
            if error >= accuracy:
                is_finished = False
        if is_finished:
            return vector, iterations
        vector = new_vector
        iterations += 1


