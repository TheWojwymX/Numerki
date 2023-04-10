from zad2 import menu
from zad2.jacobi import *


def main():
    print("\nWelcome!")
    print("\nPlease choose file to load (Remember about .txt extension!):")
    filename = input()
    if filename == "debug":
        menu.run_all_files()
        raise Exception("ALL FILES LOADED")
    try:
        loaded_matrix = menu.load_matrix_from_file(filename)
    except Exception as exception:
        raise exception
    print("\nTo choose iterations method, type 1")
    print("To choose iterations method, type 2")
    option = input()
    if option == "1":
        print("\nInsert number of iterations:")
        iterations = input()
        try:
            iterations = int(iterations)
            if iterations <= 0:
                raise Exception
        except Exception as exception:
            print("[ERROR] ITERATIONS HAVE TO BE A POSITIVE INTEGER VALUE BIGGER THAN 0")
            raise exception

        try:
            result = jacobi_method_iterations(initial_matrix=loaded_matrix, iterations=iterations)
            print(f"Solutions vector for given matrix is equal to: \n{result[0]}")
            print(f"Achieved accuracy: {result[1]}")
        except Exception as exception:
            print(exception)

    elif option == "2":
        print("\nInsert desired accuracy:")
        accuracy = input()
        try:
            last_digit = accuracy[-1]
            accuracy = float(accuracy)
            last_digit = float(last_digit)
            if last_digit != 1:
                print("[INFO] Accuracy should end in 1, assuming 1 as the final digit")
            accuracy = accuracy / last_digit
            if accuracy <= 0.0 or accuracy >= 1.0:
                raise Exception
        except Exception as exception:
            print("[ERROR] ACCURACY HAVE TO BE A POSITIVE FLOAT VALUE BETWEEN 0 AND 1 EXCLUSIVE")
            raise exception

        try:
            result = jacobi_method_accuracy(initial_matrix=loaded_matrix, accuracy=accuracy)
            print(f"Solutions vector for given matrix is equal to: \n{result[0]}")
            print(f"Result was achieved after {result[1]} iterations with accuracy {accuracy}")
        except Exception as exception:
            print(exception)
    else:
        raise Exception("[ERROR] WRONG OPTION CHOSEN")


while __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
