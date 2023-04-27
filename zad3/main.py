from zad3 import menus, lagrange_chebyshev


def main():
    print("\nWelcome!")
    menus.function_choice()
    fun = input("Choose function: ")
    if int(fun) < 0 or int(fun) > 7:
        raise Exception("Wrong function number")
    left = input("Choose the beginning of the range: ")
    right = input("Choose the end of the range: ")
    if float(left) > float(right):
        raise Exception("Wrong range selected")
    nodes = input("Choose number of nodes: ")
    if int(nodes) <= 0:
        raise Exception("Number of nodes must be greater than 0")
    lagrange_chebyshev.plotFunctions(int(nodes), float(left), float(right), int(fun))


while __name__ == "__main__":
    main()
