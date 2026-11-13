from string import ascii_uppercase


def kebabize(st):
    result = ["-" + symbol.lower() if symbol in ascii_uppercase else symbol for symbol in st if symbol.upper() in ascii_uppercase]

    if result and result[0][0] == "-":
        result[0] = result[0][1:]

    return "".join(result)


# print(kebabize("myCamelCasedString"))
# print(kebabize("myCamelHas3Humps"))
# print(kebabize("SOS"))
# print(kebabize("42"))
# print(kebabize("CodeWars"))
