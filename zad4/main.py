from Simpson import *
from Gauss_Laguerre import *


def main():
    try:
        # MENU
        print("[INFO]   Welcome!")

        choice = input("[INPUT]  Choose fuction: ")

        if choice != '1' and choice != '2' and choice != '3' and choice != '4':
            raise Exception("[ERROR]  There is no such option!")

        range_choice = input("[INPUT]  Should integral be calculated over range:\n      "
                             "   1. Selected by user\n         2. [0:inf)\n         ")
        if range_choice != '1' and range_choice != '2':
            raise Exception("[ERROR]  There is no such option!")

        if range_choice == '1':
            try:
                left = float(input("[INPUT]  Choose the beginning of the range: "))
            except Exception:
                raise Exception("[ERROR]  Left boundary must be a real number!")

            try:
                right = float(input("[INPUT]  Choose the end of the range: "))
            except Exception:
                raise Exception("[ERROR]  Right boundary must be a real number!")

            if left > right:
                raise Exception("[ERROR]  Wrong range selected")

            accuracy = input("[INPUT]  Choose the accuracy: ")
            try:
                last_digit = accuracy[-1]
                accuracy = float(accuracy)
                last_digit = float(last_digit)
                if last_digit != 1:
                    print("[INFO]   Accuracy should end in 1, assuming 1 as the final digit")
                accuracy = accuracy / last_digit
                if accuracy <= 0.0 or accuracy >= 1.0:
                    raise Exception
            except Exception as exception:
                print("[ERROR]  ACCURACY HAVE TO BE A POSITIVE FLOAT VALUE BETWEEN 0 AND 1 EXCLUSIVE")
                raise exception

            dividing_poins_amount = 1
            result = 0
            iteration = 0
            while True:
                iteration += 1
                second_result = simpsons_method(left, right, dividing_poins_amount, choice, range_choice, result)
                # print(second_result)
                if abs(second_result - result) <= accuracy:
                    result = second_result
                    break
                else:
                    result = second_result
                    dividing_poins_amount += 1

            print(f"[RESULT] Approximated integral value is equal to {result} (result achieved after {iteration} iterations)")
        if range_choice == '2':
            accuracy = input("[INPUT]  Choose the accuracy: ")
            try:
                last_digit = accuracy[-1]
                accuracy = float(accuracy)
                last_digit = float(last_digit)
                if last_digit != 1:
                    print("[INFO]   Accuracy should end in 1, assuming 1 as the final digit")
                accuracy = accuracy / last_digit
                if accuracy <= 0.0 or accuracy >= 1.0:
                    raise Exception
            except Exception as exception:
                print("[ERROR]  ACCURACY HAVE TO BE A POSITIVE FLOAT VALUE BETWEEN 0 AND 1 EXCLUSIVE")
                raise exception
            dividing_poins_amount = 1
            result = 0
            delta = 0
            left = 0
            while True:
                second_result = simpsons_method(left, left+1, dividing_poins_amount, choice, range_choice, result)
                # print(second_result[0])
                if abs(second_result[1] - delta) <= accuracy:
                    result = second_result[0]
                    break
                else:
                    result = second_result[0]
                    delta = second_result[1]
                    dividing_poins_amount += 1
            print(f"[RESULT] Approximated integral value is equal to {result} (dividing points amount: "
                  f"{dividing_poins_amount})")
            result = 0
            delta = 0
            nodes = 2
            while True:
                if nodes >5:
                    break
                delta = gaussLaguerre(nodes, choice, result)
                print(delta)
                if math.fabs(delta - result)<=accuracy:
                    result = delta
                    break
                else:
                    result += delta
                    nodes+=1

            print(f"[RESULT] Approximated integral value is equal to {result} (nodes: {nodes-1})")
    except Exception as exception:
        print(exception)
        print("[INFO]   RESTARTING ...\n\n\n")


while __name__ == "__main__":
    main()


# iteration = 2
        # dividing_points = 1

        # while True:
        #     integral_value = simpsons_method(left, right, dividing_points, choice)
        #     next_integral_value = simpsons_method(left, right, dividing_points * 2, choice)
        #     if next_integral_value - integral_value <= accuracy:
        #         break
        #     else:
        #         iteration += 1
        #         dividing_points *= 2
        #
        # print(
        #     f"[RESULT] Approximated integral value is equal to {integral_value} (result achieved after {iteration} iterations)")