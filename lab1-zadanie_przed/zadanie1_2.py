import sys


def character_substitue(text, chars):
    newtext = ''
    for i in range(len(text)):
        if text[i] in chars:
            newtext += '*'
        else:
            newtext += text[i]
    return newtext


print(character_substitue(sys.argv[1], sys.argv[2]))
