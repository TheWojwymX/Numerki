import matplotlib.pyplot as plt

from functions import *


def generateNodes(n: int):
    coeX = []
    coeY = []
    match n:
        case 2:
            coeX.extend([0.585786, 3.414214])
            coeY.extend([0.853553, 0.146447])
        case 3:
            coeX.extend([0.415775, 2.294280, 6.289945])
            coeY.extend([0.711093, 0.278518, 0.010389])
        case 4:
            coeX.extend([0.322548, 1.745761, 4.536620, 2.395071])
            coeY.extend([0.603154, 0.357419, 0.038888, 0.000539])
        case 5:
            coeX.extend([0.263560, 1.413403, 3.596426, 7.085810, 12.640801])
            coeY.extend([0.521756, 0.398667, 0.075942, 0.003612, 0.000032])
        case 6:
            coeX.extend([0.22284, 1.18893, 2.9927363, 5.77514, 9.83746, 15.98287])
            coeY.extend([0.45896, 0.41700, 0.11337, 0.010399, 0.000261, 0.00000089])
        case 7:
            coeX.extend([0.1930436, 1.026664, 2.567876, 4.90035, 8.18215, 12.73418, 19.39572])
            coeY.extend([0.40931, 0.421831, 0.147126, 0.020633, 0.001074, 0.000015, 0.000000031])
        case 8:
            coeX.extend([0.170279, 0.903701, 2.251086, 4.26670, 7.04590, 10.7585, 15.7406, 22.86313])
            coeY.extend([0.369188, 0.418786, 0.175794, 0.033343, 0.002794, 0.000090, 0.00000084, 0.0000000010])
        case 9:
            coeX.extend([0.152322, 0.807220, 2.005135, 3.783473, 6.204956, 9.372985, 13.46623, 18.83359, 26.37407])
            coeY.extend([0.336126, 0.411213, 0.199287, 0.047460, 0.005599, 0.000305, 0.0000065, 0.000000041,
                         0.000000000032])
        case 10:
            coeX.extend([0.137793, 0.729454, 1.80834, 3.40143, 5.55249, 8.33015, 11.84378, 16.27925, 21.99658,
                         29.92069])
            coeY.extend([0.308441, 0.401119, 0.218068, 0.062087, 0.009501, 0.000753, 0.000028, 0.00000042, 0.0000000018,
                         0.00000000000099])
    return coeX, coeY


def LaguerrePolynomial(n: int, x):
    Laguerre = [0] * (n + 1)
    Laguerre[0] = 1

    if n > 0:
        Laguerre[1] = x - 1

    if n > 1:
        for i in range(1, n):
            Laguerre[i + 1] = (x - 2 * i - 1) * Laguerre[i] - (i ** 2 * Laguerre[i - 1])

    return Laguerre[n]


def calculateLambda(choice: str, qDegree, pDegree):
    suma = 0
    coeX, coeY = generateNodes(qDegree)

    for i in range(qDegree):
        suma = suma + choose_function(coeX[i], choice) * coeY[i] * LaguerrePolynomial(pDegree, coeX[i])

    return suma / (math.factorial(pDegree) ** 2)


def calculateError(choice: str, qDegree, pDegree, a, b):
    coeX, coeY = generateNodes(qDegree)
    error = 0

    lambdaCoe = [0] * (pDegree + 1)
    for i in range(pDegree + 1):
        lambdaCoe[i] = calculateLambda(choice, qDegree, i)

    # Generuj punkty x dla oceny błędu aproksymacji
    x_points = np.arange(a, b + 0.01, 0.01)

    for x in x_points:
        approx_y = 0
        for j in range(pDegree + 1):
            approx_y += lambdaCoe[j] * LaguerrePolynomial(j, x)
        true_y = choose_function(x, choice)
        error += (true_y - approx_y) ** 2

    error = np.sqrt(error)

    return error


def plotFunctions(choice: str, qDegree, pDegree, left, right):
    xAxis = np.linspace(left, right)
    yAxisApprox = []
    yAxisStand = []

    lambdaCoe = [0] * (pDegree + 1)
    for i in range(pDegree + 1):
        lambdaCoe[i] = calculateLambda(choice, qDegree, i)

    for i in range(len(xAxis)):
        single_yAxis = 0
        for j in range(pDegree + 1):
            single_yAxis = single_yAxis + lambdaCoe[j] * LaguerrePolynomial(j, xAxis[i])
        yAxisApprox.append(single_yAxis)

    for i in xAxis:
        yAxisStand.append(choose_function(i, choice))

    plt.xlim(left, right)
    plt.plot(xAxis, yAxisStand, label="Funkcja oryginalna")
    plt.plot(xAxis, yAxisApprox, label="Wielomian aproksymacyjny")
    plt.legend()
    plt.savefig("plot.jpg")
    plt.show()



