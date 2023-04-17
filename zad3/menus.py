import numpy as np


def function_choice() -> None:
    print("To choose linear function, type 0")
    print("To choose absolute value function of x, type 1")
    print("To choose polynomial function, type 2")
    print("To choose trigonometric function, type 3")


def range_choice() -> tuple[np.float64, np.float64]:
    print("Choose the left bound of a function")
    try:
        left_bound = np.float64(input())
    except Exception as e:
        raise Exception("[ERROR] Not a number, restarting!")
    print("Choose the right bound of a function")
    try:
        right_bound = np.float64(input())
        if right_bound <= left_bound:
            raise Exception("[ERROR] Right bound has to be greater than left bound!")
    except Exception as e:
        raise Exception("[ERROR] Not a number, restarting!")
    return left_bound, right_bound


def slope_choice() -> np.float64:
    print("Choose the slope of the linear function")
    try:
        slope = np.float64(input())
    except Exception as e:
        raise Exception("[ERROR] Not a number, restarting!")
    return slope


def nodes_choice(nodes_amount: int) -> np.array(np.float64):
    nodes_list = np.cos((np.pi * np.arange(nodes_amount)) / nodes_amount)
    return nodes_list
