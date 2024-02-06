# Zadanie 1
def character_counter(text):
    characters_frequency = {char: text.count(char) for char in text}
    for char in characters_frequency:
        print(f"{char}: {characters_frequency[char]}")


# Zadanie 2


def character_substitute(text, characters_to_substitute):
    x = text
    for char in characters_to_substitute:
        x = x.replace(char, "*")
    return x


# Zadanie 3


def less_than_avg_removal(numbers):
    avg = sum(numbers)/len(numbers)
    return [num for num in numbers if num >= avg]


# Zadanie 4


def k_repeated(numbers):
    k_repeated_numbers = []
    for num in numbers:
        for index in range(num):
            k_repeated_numbers.append(num)
    return k_repeated_numbers


# Zadanie 5


def most_frequent_character(text):
    char_frequencies = [text.count(char) for char in text]
    max_frq = max(char_frequencies)
    most_frequent = []
    for char in text:
        if (text.count(char) == max_frq and char not in most_frequent):
            most_frequent.append(char)
    return most_frequent


# Zadanie 6


def char_index(text):
    all_chars_indices = {}
    for index_outer in range(len(text)):
        char_to_cmp = text[index_outer]
        char_indices = []
        for index_inner in range(len(text)):
            if (text[index_inner] == char_to_cmp):
                char_indices.append(index_inner)
        all_chars_indices[char_to_cmp] = char_indices
    return all_chars_indices


# Zadanie 7


def parking_spots(entries):
    spots_taken = {}
    max_scooters = 0
    for action, spot in entries:
        if action == "enter":
            spots_taken[spot] = spots_taken.get(spot, 0) + 1
        else:
            spots_taken[spot] = spots_taken.get(spot, 0) - 1
        if spots_taken[spot] > max_scooters:
            max_scooters = spots_taken[spot]
    return max_scooters


parking_spots([
    ("enter", 34),
    ("enter", 1),
    ("enter", 1),
    ("enter", 6),
    ("exit", 34),
    ("enter", 4),
    ("enter", 1),
    ("enter", 4),
    ("enter", 1),
    ("enter", 1),
    ("enter", 4),
    ("exit", 1),
])


# Zadanie 8


def characters_in_common(line1, line2):
    common = []
    for char in line1:
        if (char in line2 and char not in common):
            common.append(char)
    for char in line2:
        if (char in line1 and char not in common):
            common.append(char)
    for char in common:
        print(char)


# Zadanie 9


def mst_frequent_character(text):
    chars_frequency = [text.count(char) for char in text]
    max_frequency = max(chars_frequency)
    return max_frequency


# Zadanie 10


def avg_comparison(numbers):
    half_length = len(numbers)//2
    sum_first_half = sum(numbers[:half_length])
    sum_divided_3 = 0
    count_divided_3 = 0

    for index in range(len(numbers)):
        if index % 3:
            sum_divided_3 += numbers[index]
            count_divided_3 += 1

    avg_divided_3 = sum_divided_3/count_divided_3
    avg_first_half = sum_first_half/half_length
    return avg_divided_3 > avg_first_half


# Zadanie 11


def negative_removal(numbers):
    new_numbers = [num if num >= 0 else 0 for num in numbers]
    return new_numbers


# Zadanie 12


def nested_numbers(numbers):
    unique_numbers = []
    for nested_nums in numbers:
        for num in nested_nums:
            if num not in unique_numbers:
                unique_numbers.append(num)
    return unique_numbers

# Zadanie 13


def longest_wrd(words):
    words_lengths = [len(word) for word in words]
    max_length = max(words_lengths)
    return max_length

# Zadanie 14


def lest_than_avg_substitute(numbers):
    avg = sum(numbers) / len(numbers)
    max_num = max(numbers)
    for index in range(len(numbers)):
        num = numbers[index]
        if num < avg:
            numbers[index] = max_num
    return numbers


# Zadanie 15


def second_to_last_count(words):
    second_to_last = words[-2]
    return words.count(second_to_last)


# Zadanie 16


def even_word_length(words):
    even_words = [word for word in words if len(word) % 2 == 0]
    return len(even_words)


# Zadanie 17


def first_same_as_last_count(words):
    first_same_as_last = [word for word in words if word[0] == word[-1]]
    return len(first_same_as_last)


# Zadanie 18


def k_repeated_digits(digits):
    text = ""
    for digit in digits:
        text += str(digit) * digit
    return text


# Zadanie 19


def string_xor(text1, text2):
    return list(set(text1.lower()) ^ set(text2.lower()))


# Zadanie 20


def polish_to_latin(text):
    pl_lt = {
        "ą": "a",
        "ę": "e",
        "ć": "c",
        "ś": "s",
        "ł": "l",
        "ź": "z",
        "ż": "z"
    }
    new_text = ""
    for char in text:
        new_text += pl_lt.get(char, char)
    return new_text


# Zadanie 21


def even_vs_odd(numbers):
    even = [num for num in numbers if num % 2 == 0]
    odd = list(set(numbers) - set(even))
    return len(even) > len(odd)


# Zadanie 22


def char_counter(word):
    return {char: word.count(char) for char in word}


# Zadanie 23


def text_filter(text, char_to_filter):
    text_splitted = text.split(' ')
    char, frq = char_to_filter
    return ' '.join([word for word in text_splitted if word.count(char) < frq])


# Zadanie 24


def text_filter_2(text, chars_to_filter):
    text_splitted = text.split(' ')
    text_to_join = []

    def char_frq_check(word, chars_to_filter):
        for char, frq in chars_to_filter:
            if (word.count(char) >= frq):
                return False
        return True

    for word in text_splitted:
        if (char_frq_check(word, chars_to_filter)):
            text_to_join.append(word)

    return ' '.join(text_to_join)
