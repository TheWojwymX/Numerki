import math
import numpy as np


# n - length of array
# coe - array with polynomial's coefficients
# x - point at which we evaluate polynomial's value
def horner(n: [int], coe: [float], x: [float]) -> np.longdouble:
    result = coe[0]
    for i in range(1, n):
        result = result * x + coe[i]
    return result


# Functions:
# 1. x^3 - 6x^2 + 7x - 3
# 2. sin(3^x)
# 3. cos(x) - 2x
# 4. 5^x - 3
# 5. 4^(3 tan(0.3x^2 - 1)) - 1
# 6. sin(0.1x^2 + 12)/x
# 7. sin(2x^2 - 2) - 3x^3 + 2x^2 - 1

def function_value(x: np.longdouble, fun_num: int):
    if fun_num == 1:
        return horner(4, [1, -6, 7, -3], x)
    elif fun_num == 2:
        return math.sin(3**x)
    elif fun_num == 3:
        return math.cos(x) - 2 * x
    elif fun_num == 4:
        return 5 ** x - 3
    elif fun_num == 5:
        return 4 ** (3 * math.tan(0.3*x*x - 1)) - 1
    elif fun_num == 6:
        return math.sin(x*x + 1) / x
    elif fun_num == 7:
        return math.sin(2 * x * x - 2) + horner(4, [-3, 2, 0, -1], x)
    else:
        return 0


def bisect(fun_num: int, leftRange: np.longdouble, rightRange: np.longdouble, eps: np.longdouble = None,
           ite: int = None):
    iter_number = 0
    diff = 0
    left = leftRange
    right = rightRange
    Bi = []

    if function_value(left, fun_num) * function_value(right, fun_num) > 0:
        raise Exception("Same signs, choose different range")

    if eps is not None:
        diff = eps + 1

    while ite is not None and iter_number < ite or eps is not None and diff > eps:
        mid = (left + right) * 0.5
        mid_value = function_value(mid, fun_num)
        if mid_value * function_value(left, fun_num) <= 0:
            right = mid
        else:
            left = mid
        Bi.append((mid, mid_value))
        if len(Bi) > 2:
            diff = abs(Bi[iter_number][0] - Bi[iter_number - 1][0])
        iter_number = iter_number + 1

    return Bi


def falsi(fun_num: int, leftRange: np.longdouble, rightRange: np.longdouble, eps: np.longdouble = None,
          ite: int = None):
    iter_number = 0
    diff = 0
    left = leftRange
    right = rightRange
    Fix = []
    Fiy = []

    if function_value(left, fun_num) * function_value(right, fun_num) > 0:
        raise Exception("Same signs, choose different range")

    if eps is not None:
        diff = eps + 1

    while ite is not None and iter_number < ite or eps is not None and diff > eps:

        Fix.append((left * function_value(right, fun_num) - right * function_value(left, fun_num)) / (
                function_value(right, fun_num) - function_value(left, fun_num)))
        Fiy.append(function_value(Fix[iter_number], fun_num))

        if Fiy[iter_number] * function_value(left, fun_num) <= 0:
            right = Fix[iter_number]
        else:
            left = Fix[iter_number]

        if len(Fix) > 2:
            diff = abs(Fix[iter_number] - Fix[iter_number-1])
        iter_number = iter_number + 1


    return Fix, Fiy

