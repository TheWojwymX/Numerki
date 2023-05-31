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


def calculateError(choice: str, qDegree, pDegree):
    coeX, coeY = generateNodes(qDegree)
    suma = 0
    errorArray = [0] * qDegree

    lambdaCoe = [0] * (pDegree + 1)
    for i in range(pDegree + 1):
        lambdaCoe[i] = calculateLambda(choice, qDegree, i)

    for i in range(qDegree):
        for j in range(pDegree):
            errorArray[i] = errorArray[i] + lambdaCoe[j] * LaguerrePolynomial(j, coeX[i])

    for i in range(qDegree):
        suma = suma + coeY[i] * ((choose_function(coeX[i], choice) - errorArray[i]) ** 2)

    return math.sqrt(suma)


def plotFunctions(choice: str, qDegree, pDegree, left, right):
    xAxis = np.linspace(left, right)
    yAxisApprox = []
    yAxisStand = []

    lambdaCoe = [0] * (pDegree + 1)
    for i in range(pDegree + 1):
        lambdaCoe[i] = calculateLambda(choice, qDegree, i)
    print(lambdaCoe)

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
    plt.show()


print(calculateError('1', 5, 3))
plotFunctions('1', 5, 3, -1, 1)
