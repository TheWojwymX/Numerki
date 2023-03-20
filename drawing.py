import matplotlib.pyplot as plt
import numpy as np
import functions

# 100 linearly spaced numbers
x = np.linspace(-5, 5, 100)


def get_function_equation(function_number):
    function_equation = {1: "x^3 - 6x^2 + 7x - 3", 2: "sin(x)", 3: "cos(x)", 4: "5^x-3", 5: "4^(3 tan(0.3x^2 - 1)) - 1",
                         6: "sin(x)/x", 7: "sin(2x^2 - 2) - 3x^3 + 2x^2 - 1"}
    return function_equation.get(function_number)


def draw_function(function_number, beginning, end, precision, external_offset=0):
    bisect_x = functions.bisect(function_number, np.longdouble(beginning), np.longdouble(end),
                                np.longdouble(precision), 24)[-1][0]
    bisect_y = functions.bisect(function_number, np.longdouble(beginning), np.longdouble(end),
                                np.longdouble(precision), 24)[-1][1]
    falsi_x = \
        functions.falsi(function_number, np.longdouble(beginning), np.longdouble(end), np.longdouble(precision), 24)[0][
            -1]
    falsi_y = \
        functions.falsi(function_number, np.longdouble(beginning), np.longdouble(end), np.longdouble(precision), 24)[1][
            -1]
    plt.suptitle(get_function_equation(function_number))
    plt.title(f"Precision: {precision}")

    plt.scatter(bisect_x, bisect_y, color='blue', label="Root of function, found by Bisection method")
    plt.scatter(falsi_x, falsi_y, color="green", label="Root of function, found by Falsi method")
    plt.legend(loc="lower left")
    print(f"Bisect x:{bisect_x}\nBisect y:{bisect_y}\nFalsi x:{falsi_x}\nFalsi y:{falsi_y}")
    offset = (end - beginning+external_offset) * precision
    if bisect_x < falsi_x:
        x_inside = np.linspace(bisect_x - offset, falsi_x + offset, 100)
    if bisect_x > falsi_x:
        x_inside = np.linspace(falsi_x - offset, bisect_x + offset, 100)
    y = [functions.function_value(x_value, function_number) for x_value in x_inside]
    plt.axhline(0, color='black')
    plt.plot(x_inside, y, scalex=True)

    plt.show()


draw_function(1, x[0], x[-1], 0.0000000001)  # ok
draw_function(2, x[0], x[-1], 0.0001)  # ok
# cosine is borken
# draw_function(3, -1.5 * np.pi, 1.5 * np.pi, 0.00001) not ok
draw_function(4, x[0], x[-1], 0.0001)  # ok
# draw_function(5,x[0],x[-1],0.00001) not ok
# draw_function(6, x[0], x[-1], 0.00001) 0?
draw_function(7, x[0], x[-1], 0.0001)  # ok
