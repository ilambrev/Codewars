def changer(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    result = []

    for symbol in s.lower():
        index = alphabet.find(symbol)

        if index > -1:
            index = (index + 1) % 26
            symbol = alphabet[index]

        if symbol in vowels:
            symbol = symbol.upper()

        result.append(symbol)

    return "".join(result)


# print(changer("Cat30"))
# print(changer("Alice"))
# print(changer("sponge1"))
# print(changer("Hello World"))
# print(changer("dogs"))
# print(changer("z"))
