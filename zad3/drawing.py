import numpy as np
from matplotlib import pyplot as plt


def draw_initial_function(x_values: np.array, y_values: np.array) -> None:
    plt.plot(x_values, y_values, label="Function")
    plt.show()
