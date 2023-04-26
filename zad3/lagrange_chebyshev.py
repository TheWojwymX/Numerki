import numpy as np
import matplotlib.pyplot as plt
import functions


# Define the function to be interpolated
def function(funNumber, x):
    if funNumber == 1:
        return x - 1
    if funNumber == 2:
        return abs(x)
    if funNumber == 3:
        return functions.horner(3, [-0.5, 2, 1, 3], x)
    if funNumber == 4:
        return np.sin(x)
    if funNumber == 5:
        return np.cos(functions.horner(3, [-0.5, 2, 1, 3], x) - 2 * x)
    if funNumber == 6:
        return abs(np.cos(x))
    if funNumber == 7:
        return abs(np.sin(3, [-1, 2, 1, 3], x))


# Generate Chebyshev nodes
def generateNodes(numberOfNodes, minRange, maxRange, functionNumber):
    Nx = []
    Ny = []
    i = 0
    while i < numberOfNodes:
        Nx.append(0.5*(maxRange+minRange) + 0.5*(maxRange-minRange)*np.cos(np.pi*(i+0.5)/numberOfNodes))
        Ny.append(function(functionNumber, Nx[i]))
        i = i + 1
    return Nx, Ny


# Compute the function values at the interpolation points
def calculateInterpolation(numberOfNodes, minRange, maxRange, functionNumber):
    Ix = []
    Iy = []
    i = minRange
    while i < maxRange:
        y = 0
        for j in range(numberOfNodes):
            temp = generateNodes(numberOfNodes, minRange, maxRange, functionNumber)[1][j]
            for k in range(numberOfNodes):
                if j != k:
                    temp = temp * ((i - generateNodes(numberOfNodes, minRange, maxRange, functionNumber)[0][k])
                                   / (generateNodes(numberOfNodes, minRange, maxRange, functionNumber)[0][j] -
                                      generateNodes(numberOfNodes, minRange, maxRange, functionNumber)[0][k]))
            y = y + temp
        Ix.append(i)
        Iy.append(y)
        i = i + 0.1
    return Ix, Iy


def plotFunctions(numberOfNodes, minRange, maxRange, functionNumber) -> None:
    x_range = np.linspace(minRange, maxRange, 100)
    plt.plot(x_range, function(functionNumber, x_range), label="Function")
    plt.plot(calculateInterpolation(numberOfNodes, minRange, maxRange, functionNumber)[0],
             calculateInterpolation(numberOfNodes, minRange, maxRange, functionNumber)[1],
             label="Interpolation")
    plt.scatter(generateNodes(numberOfNodes, minRange, maxRange, functionNumber)[0],
                generateNodes(numberOfNodes, minRange, maxRange, functionNumber)[1],
                c='red', label="Interpolation Points")
    plt.legend()
    plt.savefig("Plot.jpg")
    plt.show()
