import math
import functions


def gaussLaguerre(nodes: int, choice: str) -> float:
    dictionary = dict()
    result = 0
    match nodes:
        case 2:
            dictionary = {0.585786: 0.853553, 3.41421: 0.146447}
        case 3:
            dictionary = {0.415775: 0.711093, 2.2943: 0.278518, 6.28995: 0.0103893}
        case 4:
            dictionary = {0.322548: 0.603154, 1.74576: 0.357419, 4.53662: 0.038888, 9.3951: 0.000539295}
        case 5:
            dictionary = {0.26356: 0.521756, 1.4134: 0.398667, 3.59643: 0.075942, 7.08581: 0.00361176,
                          12.6408: 0.00002337}

    for i in range(0, nodes - 1):
        result += list(dictionary.values())[i] * functions.choose_function(list(dictionary)[i], choice) / math.exp(-list(dictionary)[i])

    return result
