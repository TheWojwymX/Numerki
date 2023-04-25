from zad3 import menus, functions, drawing


def main():
    print("\nWelcome!")
    menus.function_choice()
    try:
        option = int(input())
        if 0 > option > 3:
            raise Exception("[ERROR] Incorrect option!")
    except Exception:
        raise Exception("[ERROR] Not a numeric option!")
    try:
        left_bound, right_bound = menus.range_choice()
    except Exception as exception:
        raise exception
    initial_x = functions.get_x_values(left_bound, right_bound)
    nodes_amount = 10
    nodes_list = menus.nodes_choice(nodes_amount)

    match option:
        case 0:
            try:
                slope = menus.slope_choice()
                initial_y = functions.get_y_linear(slope, initial_x)
            except Exception as e:
                raise e
            drawing.draw_initial_function(initial_x, initial_y)
        case 1:
            print("Not implemented yet")
        case 2:
            print("Not implemented yet")
        case 3:
            print("Not implemented yet")


while __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
