import numpy as np


def horner(n: [int], coe: [float], x: [float]) -> np.longdouble:
    result = coe[0]
    for i in range(1, n):
        result = result * x + coe[i]
    return result
