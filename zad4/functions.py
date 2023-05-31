import math


def choose_function(x: float, choice: str) -> float:
    match choice:
        case '1':
            return (5 * x - 2) * math.e ** -x
        case '2':
            return (x ** 3 + 5 * x ** 2 - 4 * x + 20) * math.e ** -x
        case '3':
            return (math.sin(x)) * math.e ** -x
        case '4':
            return abs(x ** 2 - 8 + math.cos(x)) * math.e ** -x

def menu():
    print("1. (5x - 2) * e^(-x)")
    print("2. (x^3 + 5x^2 - 4x + 20) * e^(-x)")
    print("3. sin(x) * e^(-x)")
    print("4. |x^2 - 8 + cos(x)| * e^(-x)")

