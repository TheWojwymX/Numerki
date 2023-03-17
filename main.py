from functions import *
from menus import *


def main():
    print(falsi(1, 0, 5, eps=0.0000001))
    # choose_function()
    # while 1:
    #     fun = int(input("Function: "))
    #     range1 = np.longdouble(input("Left range: "))
    #     range2 = np.longdouble(input("Right range: "))
    #     option = int(input("Stop condition: 1 - epsilon, 2 - iterations: "))
    #
    #     if option == 1:
    #         eps = np.longdouble(input("Epsilon value: "))
    #         print("Bisect method:")
    #         print(bisect(fun, range1, range2, eps=eps))
    #         print("Falsi method:")
    #         print(falsi(fun, range1, range2, eps=eps))
    #
    #     if option == 2:
    #         ite = int(input("Number of iterations: "))
    #         print("Bisect method:")
    #         print(bisect(fun, range1, range2, ite=ite))
    #         print("Falsi method:")
    #         print(falsi(fun, range1, range2, ite=ite))


if __name__ == '__main__':
    main()
