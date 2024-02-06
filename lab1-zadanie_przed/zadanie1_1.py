import sys


def character_counter(text):
    chars = []
    for i in text:
        if i not in chars:
            chars.append(i)
    for i in chars:
        print(i + ": " + str(text.count(i)))


character_counter(sys.argv[1])
