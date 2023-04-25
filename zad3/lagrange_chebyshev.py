import numpy as np
import matplotlib.pyplot as plt
import math

Nx = []
Ny = []
Ix = []
Iy = []


# Define the function to be interpolated
def function(x):
    return x*x + 2

# Generate Chebyshev nodes
def generateNodes(numberOfNodes, minRange, maxRange, functionNumber):
    i = 0
    while i < numberOfNodes:
        Nx.append(((maxRange - minRange) * math.cos(math.pi * (2 * i + 1) / (2 * numberOfNodes + 1))) * (
                    minRange + maxRange) * 0.5)
        Ny.append(function(Nx[i]))
        i = i + 1


# Compute the function values at the interpolation points
def calculateInterpolation(numberOfNodes, minRange, maxRange, functionNumber):
    i = minRange
    while i < maxRange:
        y = 0
        for j in range(numberOfNodes):
            temp = Ny[j]
            for k in range(numberOfNodes):
                if j != k:
                    temp = temp * ((i - Nx[k]) / (Nx[j] - Nx[k]))
            y = y + temp
        Ix.append(i)
        Iy.append(y)
        i = i + 0.1

# Test
generateNodes(10, 2, 4, 1)
calculateInterpolation(10, 2, 4, 1)

# Compute the interpolated values over a range of x values
x_range = np.linspace(-np.pi, np.pi, 1000)
y_range = np.zeros(1000)
for i in range(5):
    y_range[i] = Iy[i]

# Plot the function and its interpolation
plt.plot(x_range, function(x_range), label="Function")
plt.scatter(Nx, Ny, c='red', label="Interpolation Points")
plt.legend()
plt.show()
plt.plot(Ix, Iy, label="Interpolation")
plt.legend()
plt.show()
plt.plot(x_range, function(x_range), label="Function")
plt.plot(Ix, Iy, label="Interpolation")
plt.scatter(Nx, Ny, c='red', label="Interpolation Points")
plt.legend()
plt.show()
