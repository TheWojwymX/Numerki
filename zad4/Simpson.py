import functions


# def simpsons_method(x_start, x_end, dividing_poins_amount, choice):
#     integral_value = 0
#     integral_value_between_points = 0
#
# distance_between_points = (x_end - x_start) / dividing_poins_amount for i in range(1, dividing_poins_amount + 1):
# x_of_dividing_point = x_start + i * distance_between_points integral_value_between_points +=
# functions.choose_function( x_of_dividing_point - distance_between_points / 2, choice) if i < dividing_poins_amount:
# integral_value = integral_value + functions.choose_function(x_of_dividing_point, choice) integral_value =
# distance_between_points / 6 * ( functions.choose_function(x_start, choice) + functions.choose_function(x_end,
# choice) + 2 * integral_value + 4 * integral_value_between_points)
#
#     return integral_value

def simpsons_method(x_start, x_end, dividing_poins_amount, choice, choice2, result):
    distance_between_points = (x_end - x_start) / dividing_poins_amount

    sum1 = 0
    sum2 = 0
    for i in range(1, dividing_poins_amount):
        x = x_start + i * distance_between_points
        sum1 += functions.choose_function(x - distance_between_points / 2.0, choice)
        sum2 += functions.choose_function(x, choice)

    sum1 += functions.choose_function(x_end - distance_between_points / 2.0, choice)
    if choice2 == '1':
        result = ((x_end - x_start) / (6.0 * dividing_poins_amount)) * (
                functions.choose_function(x_start, choice) + functions.choose_function(x_end,
                                                                                       choice) + 2 * sum2 + 4 * sum1)
        return result
    else:
        result_2 = ((x_end - x_start) / (6.0 * dividing_poins_amount)) * (
                functions.choose_function(x_start, choice) + functions.choose_function(x_end,
                                                                                       choice) + 2 * sum2 + 4 * sum1)
        result += result_2
        return result, result_2
