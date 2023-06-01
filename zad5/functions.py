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
            return abs(x-2)
        case '4':
            return math.cos(x)
        case '5':
            return math.sin(horner(4, [2.0, -4.0, 8.0, -3.0], x))
        case '6':
            return abs(0.5*x - math.cos(x*x))

def printMenu():
    print("Wybierz funkcje: ")
    print("1. x+1")
    print("2. 2x^3 - 4x^2 + 8x - 3 ")
    print("3. |x-2|")
    print("4. cos(x)")
    print("5. sin(2x^3 - 4x^2 + 8x - 3)")
    print("6. |0.5x - cos(x^2)|")
