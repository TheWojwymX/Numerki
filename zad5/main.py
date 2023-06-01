from approximation import *


def main():
    printMenu()
    fun = input()
    if int(fun) < 1 or int(fun) > 6:
        raise Exception("Wrong function number")

    left = float(input("Podaj początek przedziału aproksymacji: "))
    right = float(input("Podaj koniec przedziału aproksymacji: "))

    if left > right:
        raise Exception("Wrong range selected")

    pDegree = int(input("Podaj stopień wielomianu aproksymacyjnego: "))
    if pDegree < 1:
        raise Exception("Wrong polynomial degree")

    qDegree = int(input("Podaj liczbę węzłów do całkowania metodą Gaussa-Laguerre: "))
    if qDegree < 2 or qDegree > 10:
        raise Exception("Wrong quadrature degree")

    plotFunctions(fun, qDegree, pDegree, left, right)


if __name__ == "__main__":
    main()
