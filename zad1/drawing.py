import matplotlib.pyplot as plt
import numpy as np
import functions

# 100 linearly spaced numbers


def get_function_equation(function_number):
    function_equation = {1: "x^3 - 6x^2 + 7x - 3", 2: "sin(3^x)", 3: "cos(x)-2x",
                         4: "5^x-3", 5: "4^(3 tan(0.3x^2 - 1)) - 1",
                         6: "sin(x^2 + 1)/x", 7: "sin(2x^2 - 2) - 3x^3 + 2x^2 - 1"}
    return function_equation.get(function_number)


def draw_function(function_number, beginning, end, name, precision=None, iterations=None, external_offset=0):
    if precision is None:
        precision=0.1
    if iterations is None:
        iterations=1
    bisect_x = functions.bisect(function_number, np.longdouble(beginning), np.longdouble(end),
                                np.longdouble(precision), iterations)[-1][0]
    bisect_y = functions.bisect(function_number, np.longdouble(beginning), np.longdouble(end),
                                np.longdouble(precision), iterations)[-1][1]
    falsi_x = \
        functions.falsi(function_number, np.longdouble(beginning), np.longdouble(end), np.longdouble(precision),
                        iterations)[0][-1]
    falsi_y = \
        functions.falsi(function_number, np.longdouble(beginning), np.longdouble(end), np.longdouble(precision),
                        iterations)[1][-1]
    iterBisect = len(functions.bisect(function_number, np.longdouble(beginning), np.longdouble(end),
                                      np.longdouble(precision), iterations))
    iterFalsi = len(
        functions.falsi(function_number, np.longdouble(beginning), np.longdouble(end), np.longdouble(precision),
                        iterations)[0])
    plt.suptitle(get_function_equation(function_number))
    plt.title(f"Precision: {precision}")

    plt.scatter(bisect_x, bisect_y, color='blue', label="Root of function, found by Bisection method")
    plt.scatter(falsi_x, falsi_y, color="green", label="Root of function, found by Falsi method")
    plt.legend(loc="lower left")
    print(f"Bisect x:{bisect_x}\nBisect y:{bisect_y}\nIterations:{iterBisect}\nFalsi x:{falsi_x}\nFalsi y:{falsi_y}\nIterations:{iterFalsi}")
    offset = (end - beginning+external_offset) * precision
    if bisect_x < falsi_x:
        x_inside = np.linspace(bisect_x - offset, falsi_x + offset, 200)
    elif bisect_x > falsi_x:
        x_inside = np.linspace(falsi_x - offset, bisect_x + offset, 200)
    else:
        x_inside = np.linspace(falsi_x - offset, falsi_x + offset, 200)
    y = [functions.function_value(x_value, function_number) for x_value in x_inside]
    plt.axhline(0, color='black')
    plt.plot(x_inside, y, scalex=True)

    plt.savefig(name+'.jpg')
    plt.clf()


# draw_function(1, 4.5, 5.0, name='f1_iter', iterations=10)
# draw_function(1, 4.5, 5.0, name='f1_eps', precision=0.01)
# draw_function(1, 4.5, 5.0, name='f1_eps_2', precision=0.0001)
# draw_function(2, 0, 1.5, name='f2_iter', iterations=10)  # ok
# draw_function(2, 0, 1.5, name='f2_eps', precision=0.01)  # ok
# draw_function(2, 0, 1.5, name='f2_eps_2', precision=0.0001)  # ok
# draw_function(3, 0, 1, name='f3_iter', iterations=10)
# draw_function(3, 0, 1, name='f3_eps', precision=0.01)
# draw_function(3, 0, 1.5, name='f3_eps_2', precision=0.0001)  # ok
# draw_function(4, 0, 1, name='f4_iter', iterations=10)
# draw_function(4, 0, 3, name='f4_eps', precision=0.01)
# draw_function(4, 0, 3, name='f4_eps_2', precision=0.0001)  # ok
# draw_function(5, 0, 2, name='f5_iter', iterations=10)
# draw_function(5, 0, 2, name='f5_eps', precision=0.01)
# draw_function(5, 0, 2, name='f5_eps_2', precision=0.0001)
# draw_function(6, 1, 1.5, name='f6_iter', iterations=10)
# draw_function(6, 1, 1.5, name='f6_eps', precision=0.01)
# draw_function(6, 1, 1.5, name='f7_eps_2', precision=0.0001)
draw_function(7, -3, 0, name='f7_iter', iterations=10)
draw_function(7, -3, 0, name='f7_eps', precision=0.01)
draw_function(7, -3, 0, name='f7_eps_2', precision=0.0001)
#
