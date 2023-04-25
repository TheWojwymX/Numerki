import numpy as np


def horner(n: [int], coe: [float], x: [float]) -> np.longdouble:
    result = coe[0]
    for i in range(1, n):
        result = result * x + coe[i]
    return result


def get_x_values(left_bound: np.float64, right_bound: np.float64) -> np.array:
    x_initial_values = np.linspace(left_bound, right_bound, 1000)
    return x_initial_values


def get_y_linear(a: np.float64, x_values: np.array) -> np.array:
    y_initial_values = a * x_values
    return y_initial_values


# TODO:FIX THIS CAUSE NOT WORKING
def lagrange(x_value: np.float64, initial_y: np.array, nodes_amount: int, nodes_list: np.array):
    L = np.zeros(nodes_amount)
    for i in range(nodes_amount):
        p = 1
        for j in range(nodes_amount):
            if j != i:
                p *= (x_value - nodes_list[j]) / (nodes_list[i] - nodes_list[j])
        L[i] = p
    return np.dot(initial_y, L)
