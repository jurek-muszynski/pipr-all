# Zadanie 1


def admin_names_print(names):
    for name in names:
        print(name)

# Zadanie 2


def admin_exists(sites):
    return "Ervin Howell" in sites and "John Smith" not in sites

# Zadanie 3


def admins_longitude(admins):
    return {admin["name"]: admin["address"]["geo"]["lng"] for admin in admins}

# Zadanie 4


def character_frq(word):
    return {character: word.count(character) for character in word}

# Zadanie 5


def text_filter(text, char_frq):
    letter, frq = char_frq
    text_split = text.split(' ')
    return ' '.join([word for word in text_split if word.count(letter) < frq])

# Zadanie 6


def text_filter_2(text, char_frq_list):
    text_split = text.split(' ')
    return ' '.join([word for word in text_split if False not in [word.count(letter) < frq for letter, frq in char_frq_list]])

# Zadanie 7


def characters_remove(characters, title_to_delete):
    return [character for character in characters if character[0] != title_to_delete]
