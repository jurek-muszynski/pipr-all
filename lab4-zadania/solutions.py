# Zadanie 1

def char_counter(text):
    char_frqs = {letter: text.count(letter) for letter in text}
    for letter in char_frqs:
        print(f"{letter}: {char_frqs[letter]}")


# Zadanie 2


def char_substitute(text, chars):
    new_text = ""
    for char in text:
        if char in chars:
            new_text += '*'
        else:
            new_text += char
    return new_text

# Zadanie 3


def more_than_avg(num_list):
    return [num for num in num_list if num >= (sum(num_list)/len(num_list))]


# Zadanie 4

def k_repeated(num_list):
    new_num_list = []
    for num in num_list:
        for i in range(num):
            new_num_list.append(num)
    return new_num_list

# Zadanie 5


def salary(dict1, dict2):
    desctructured_d1 = {person: dict1.get(person, 0)
                        [0]*dict1.get(person, 0)[1] for person in dict1}
    desctructured_d2 = {person: dict2.get(person, 0)
                        [0]*dict2.get(person, 0)[1] for person in dict2}

    return {person: desctructured_d1[person]+desctructured_d2[person]
            for person in desctructured_d1}

# Zadanie 6


def mst_frq_char(text):
    chars_freqency = [text.count(char) for char in text]
    max_frequency = max(chars_freqency)
    mst_frequent_chars = {char: text.count(char)
                          for char in text if text.count(char) == max_frequency}
    for char in mst_frequent_chars:
        print(f"'{char}': {max_frequency}")
