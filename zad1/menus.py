import drawing


def choose_function():
    print("Made by Jakub Kalinowski & Piotr Marszałek")
    print("Choose your function:")
    for i in range(1,8):
        print(f"{i}: {drawing.get_function_equation(i)}")
    print("To exit the applcation, type exit\n")


def choose_stop():
    print("Choose your stop condition:")
    print("1. Precision")
    print("2. Iterations")

