import numpy as np
import math


def horner(n: [int], coe: [float], x: [float]) -> np.longdouble:
    result = coe[0]
    for i in range(1, n):
        result = result * x + coe[i]
    return result


def choose_function(x: float, choice: str) -> float:
    match choice:
        case '1':
            return x+1
        case '2':
            return horner(4, [2.0, -4.0, 8.0, -3.0], x)
        case '3':
            return abs(x)
        case '4':
            return math.cos(x)
        case '5':
            return math.sin(horner(4, [2.0, -4.0, 8.0, -3.0], x))
        case '6':
            return abs(3*x - math.cos(x*x))


