import numpy as np
import matplotlib.pyplot as plt


# Define the function to be interpolated
def function(funNumber, x):
    if funNumber == 1:
        return x - 1
    if funNumber == 2:
        return abs(x)
    if funNumber == 3:
        return horner(4, [-0.5, 2, 1, 3], x)
    if funNumber == 4:
        return np.sin(x)
    if funNumber == 5:
        return np.cos(horner(4, [-0.5, 2, 1, 3], x))
    if funNumber == 6:
        return abs(np.cos(x))
    if funNumber == 7:
        return abs(np.sin(horner(4, [-0.5, 2, 1, 3], x)))


def horner(n: [int], coe: [float], x: [float]) -> np.longdouble:
    result = coe[0]
    for i in range(1, n):
        result = result * x + coe[i]
    return result


# Generate Chebyshev nodes
def generateNodes(numberOfNodes, minRange, maxRange, functionNumber):
    Nx = []
    Ny = []
    i = 0
    while i < numberOfNodes:
        Nx.append(0.5 * (maxRange + minRange) + 0.5 * (maxRange - minRange) * np.cos(np.pi * (i + 0.5) / numberOfNodes))
        Ny.append(function(functionNumber, Nx[i]))
        i = i + 1
    return Nx, Ny


# def loadNodes(file):
#     data = np.loadtxt(file, delimiter=' ')
#     Nx = np.ndarray.tolist(data[:, 0])
#     Ny = np.ndarray.tolist(data[:, 1])
#     return Nx, Ny

# Compute the function values at the interpolation points
def calculateInterpolation(numberOfNodes, minRange, maxRange, functionNumber):
    Ix = []
    Iy = []
    Nodes = generateNodes(numberOfNodes, minRange, maxRange, functionNumber)
    i = minRange
    while i < maxRange:
        y = 0
        for j in range(numberOfNodes):
            temp = Nodes[1][j]
            for k in range(numberOfNodes):
                if j != k:
                    temp = temp * ((i - Nodes[0][k]) / (Nodes[0][j] - Nodes[0][k]))
            y = y + temp
        Ix.append(i)
        Iy.append(y)
        i = i + 0.01
    return Ix, Iy


def plotFunctions(numberOfNodes, minRange, maxRange, functionNumber) -> None:
    x_range = np.linspace(minRange, maxRange, 100)
    Interpolation = calculateInterpolation(numberOfNodes, minRange, maxRange, functionNumber)
    Nodes = generateNodes(numberOfNodes, minRange, maxRange, functionNumber)
    plt.plot(x_range, function(functionNumber, x_range), label="Function")
    plt.plot(Interpolation[0],
             Interpolation[1],
             label="Interpolation")
    plt.scatter(Nodes[0],
                Nodes[1],
                c='red', label="Interpolation Points")
    plt.legend()
    plt.savefig("Plot.jpg")
    plt.show()
