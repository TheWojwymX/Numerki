import numpy as np
import matplotlib.pyplot as plt

# Define the function to be interpolated
def f(x):
    return np.cos(x)

# Set the number of interpolation points
n = 10

# Generate Chebyshev nodes
x = np.cos((np.pi*np.arange(n))/n)

# Compute the function values at the interpolation points
y = f(x)

# Define the Lagrange interpolating polynomial
def lagrange(x0):
    L = np.zeros(n)
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p *= (x0 - x[j])/(x[i] - x[j])
        L[i] = p
    return np.dot(y, L)

# Compute the interpolated values over a range of x values
x_range = np.linspace(-np.pi, np.pi, 1000)
y_range = np.zeros(1000)
for i in range(1000):
    y_range[i] = lagrange(x_range[i])

# Plot the function and its interpolation
plt.plot(x_range, f(x_range), label="Function")
plt.scatter(x, y, c='red', label="Interpolation Points")
plt.legend()
plt.show()
plt.plot(x_range, y_range, label="Interpolation")
plt.legend()
plt.show()
plt.plot(x_range, f(x_range), label="Function")
plt.plot(x_range, y_range, label="Interpolation")
plt.scatter(x, y, c='red', label="Interpolation Points")
plt.legend()
plt.show()