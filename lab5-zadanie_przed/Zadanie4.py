char_array = [[chr(((index+k) % 26)+65) for index in range(26)]
              for k in range(26)]


def encrypt_vigenere(plain_text, key):
    new_plain_text = ""
    plain_text_no_spaces = ''.join(plain_text.split(" "))
    cypher = ""

    new_plain_text += key
    counter = 0
    for index in range(1, len(plain_text)):
        if (plain_text[index] == " "):
            new_plain_text += " "
        else:
            new_plain_text += plain_text_no_spaces[(counter) %
                                                   len(plain_text_no_spaces)]
            counter += 1
    for index in range(len(new_plain_text)):
        if (new_plain_text[index]) != " ":
            cypher += char_array[ord(new_plain_text[index]) -
                                 65][ord(plain_text[index]) - 65]
        else:
            cypher += " "
    return cypher


def decrypt_vigenere(cypher, key):
    plain_text = char_array[ord(cypher[0])-65][ord(key)-65]
    counter = 0
    decrypt_key = char_array[ord(cypher[0])-65][ord(key)-65]
    for index in range(1, len(cypher)):
        if (cypher[index]) != " ":
            plain_text += char_array[ord(cypher[index]) -
                                     65][ord(decrypt_key[counter]) - 65]
            counter += 1
        else:
            plain_text += " "
    print(plain_text)


decrypt_vigenere(encrypt_vigenere(
    "TO JEST BARDZO TAJNY TEKST", "N"), "N")
