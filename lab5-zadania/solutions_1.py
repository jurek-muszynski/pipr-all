# Zadanie 1


def char_print(rows):
    chars = ""
    for i in range(rows):
        chars += "$" if (i % 2) else "*"
        print(chars)


# Zadanie 2


def pickle_delivery(delivery_list):
    pickles_sum = 0
    for delivery in delivery_list:
        if (delivery["name"] == "ogórek"):
            pickles_sum += delivery["mass"]
    return pickles_sum


# Zadanie 3


def weight_print(weights_names):
    weights = {
        "Duży Karol": 2000,
        "Ag 125": 125,
        "USA-1lb": 453.59
    }

    for weight_name in weights_names:
        if (weights[weight_name] > 1000):
            print(f"{weight_name} 1000g")
        else:
            print(f"{weight_name} {weights[weight_name]}g")


# Zadanie 4


def odd_sum_check(num_list):
    sum_odd = 0
    sum_3_dividable = 0
    for index in range(len(num_list)):
        if (index + 1) % 2:
            sum_odd += num_list[index]
        if (index + 1) % 3 == 0:
            sum_3_dividable += num_list[index]
    return sum_odd > sum_3_dividable

# Zadanie 5


def chars_indices(text):
    char_indices = {}
    for i in range(len(text)):
        indices = []
        for j in range(len(text)):
            if (text[i] == text[j]):
                indices.append(j)
        if (text[i] != " "):
            char_indices[text[i]] = indices
    return char_indices

# Zadanie 6


def parking_monitor(entries):
    taken_spots = {}
    max_scooters = 0
    for action, number in entries:
        if action == "enter":
            currently = taken_spots.get(number, 0) + 1
            taken_spots[number] = currently
        else:
            currently = taken_spots.get(number, 0) - 1
            taken_spots[number] = currently
        if (currently > max_scooters):
            max_scooters = taken_spots[number]
    return max_scooters


# Zadanie 7


def chars_print(line1, line2):
    common = []
    for char in line1:
        if (char in line1 and char in line2 and char not in common):
            print(char)
            common.append(char)

# Zadanie 8


def mst_frequent(text):
    char_frq_list = [text.count(char) for char in text]
    return max(char_frq_list)


# Zadanie 9


def avg_comparator(nums):
    div_3_sum = 0
    div_3_counter = 0
    split_half_sum = sum(nums[:(len(nums)//2)])
    split_half_avg = split_half_sum/(len(nums)/2)
    for index in range(len(nums)):
        if index % 3 == 1:
            div_3_sum += nums[index]
            div_3_counter += 1
    return (div_3_sum/div_3_counter) > split_half_avg

# Zadanie 10


def salary_calculator(first_project, second_project):
    salary_combined = {}
    for project in first_project, second_project:
        for person in project:
            salary_combined[person] = salary_combined.get(
                person, 0) + (project[person][0] * project[person][1])
    for person in salary_combined:
        salary_combined[person] = f"{salary_combined[person]:.2f}"
    return salary_combined

# Zadanie 11


def negative_substitue(nums):
    return [num if num >= 0 else 0 for num in nums]


# Zadanie 12


def tuples_of_numbers(nums):
    all_nums = []
    for inner_nums in nums:
        for num in inner_nums:
            if (num not in all_nums):
                all_nums.append(num)
    return all_nums

# Zadanie 13


def longest_word(words):
    words_lengths = [len(word) for word in words]
    return max(words_lengths)

# Zadanie 14


def number_substitue(nums):
    max_num = max(nums)
    avg_nums = sum(nums)/len(nums)
    return [num if num >= avg_nums else max_num for num in nums]


# Zadanie 15


def second_to_last(words):
    second_to_last_word = words[-2]
    return words.count(second_to_last_word)


# Zadanie 16


def even_word_length(words):
    counter = 0
    for word in words:
        if (len(word) % 2 == 0):  # % 5 == 0
            counter += 1
    return counter

# Zadanie 17


def avg_substitute(nums):
    avg = sum(nums)/len(nums)
    return [num if num >= avg else 0 for num in nums]

# Zadanie 18


def first_same_as_last(words):
    counter = 0
    for word in words:
        if (word[0] == word[-1]):
            counter += 1
    return counter


# Zadanie 19


def digit_multiplier(nums):
    combined_digits = ''
    for num in nums:
        for index in range(num):
            combined_digits += str(num)
    return combined_digits


# Zadanie 20


def char_in_only_one(word1, word2):
    chars = []
    for char in word1.lower():
        if (char not in word2):
            chars.append(char)
    for char in word2.lower():
        if (char not in word1):
            chars.append(char)
    return chars

# Zadanie 21


def polish_to_latin(word):
    pl_lt = {
        "ą": "a",
        "ę": "e",
        "ć": "c",
        "ś": "s",
        "ź": "z",
        "ó": "o",
        "ł": "l",
        "ż": "z"
    }
    substituted_word = ""
    for char in word:
        substituted_word += pl_lt.get(char, char)
    return substituted_word

# Zadanie 22


def even_vs_odd(nums):
    even_ln = len([num for num in nums if num % 2 == 0])
    odd_ln = len([num for num in nums if num % 2])
    return even_ln > odd_ln


# Zadanie 23


def check_character_percentage(text):
    return {char: text.count(char)/len(text) for char in text}


# Zadanie 24


def matrix_sums(matrix):
    column_sum = 0
    row_sum = 0
    diagonal_sum = 0
    dim = len(matrix)
    for i in range(dim):
        for j in range(dim):
            row_sum += matrix[i][j]
            column_sum += matrix[j][i]
        diagonal_sum += (matrix[i][i]) + (matrix[dim-i-1][i])
    return (diagonal_sum, row_sum, column_sum)


# Zadanie 25


def words(dictionary):
    lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    return {item: dictionary[item] for item in
            dictionary if dictionary[item][-1] in lst}
