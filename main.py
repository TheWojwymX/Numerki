import drawing
import functions
import menus
import numpy as np

while True:
    menus.choose_function()
    option = input()
    if option.upper() == 'EXIT':
        break
    elif not option.isdigit() or int(option) < 1 or int(option) > 7:
        print("WRONG VALUE ENTERED")
    else:
        beginning = input("Enter beginning of the interval\n")
        if not beginning.strip('-').isnumeric():
            print("WRONG VALUE ENTERED")
            break
        end = input("Enter end of the interval\n")
        if not end.strip('-').isnumeric():
            print("WRONG VALUE ENTERED")
            break
        name_to_save = input("Name the output file (without extension)\n")
        menus.choose_stop()
        stop_parameter = input()

        if stop_parameter == '1':
            precision = input("Insert precision value\n")
            if not precision.isnumeric():
                print("WRONG VALUE ENTERED")
                break
            else:
                drawing.draw_function(int(option), np.longdouble(beginning), np.longdouble(end), name_to_save,
                                      precision=np.longdouble(precision))
        elif stop_parameter == '2':
            iterations = input("Insert iterations amount\n")
            if not iterations.isnumeric():
                print("WRONG VALUE ENTERED")
                break
            else:
                drawing.draw_function(int(option), np.longdouble(beginning), np.longdouble(end), name_to_save,
                                      iterations=np.longdouble(iterations))
        else:
            print("WRONG VALUE ENTERED")
            break
