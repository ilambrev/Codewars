def AlphaNum_NumAlpha(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    number = ""

    for symbol in string:
        if symbol in alphabet:
            if number:
                result += alphabet[int(number)-1]
                number = ""
            index = alphabet.index(symbol)
            result += str(index + 1)
        else:
            number += symbol

    if number:
        result += alphabet[int(number)-1]

    return result


# print(AlphaNum_NumAlpha('25abcd26'))
# print(AlphaNum_NumAlpha('18zyz14'))
# print(AlphaNum_NumAlpha('a1b2c3d4'))
# print(AlphaNum_NumAlpha('5a8p17'))
