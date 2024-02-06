def count_average(numbers):
    return sum(numbers)/len(numbers)


def count_element_above_average(numbers):
    average = count_average(numbers)
    numbers_above_average = len([num for num in numbers if num > average])
    return numbers_above_average


def count_elements_above_average(list_of_numbers):
    results_list = []
    for numbers in list_of_numbers:
        try:
            result = count_element_above_average(numbers)
        except ZeroDivisionError:
            result = "DZIELENIE PRZEZ ZERO"
        except TypeError:
            result = "ZŁA WARTOŚĆ"
        results_list.append(result)
    return results_list


print(count_elements_above_average(
    [[1, 2, 3], [5, 6, 7], [], [3, 4, 5], ["12a", 1, 4]]))
