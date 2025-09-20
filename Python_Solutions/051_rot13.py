def rot13(message):
    encoded_symbols = []

    for i in range(len(message)):
        ascii_value = ord(message[i])
        symbol = message[i]
        if 65 <= ascii_value <= 90:
            ascii_value = (ascii_value + 13
                           if ascii_value + 13 <= 90
                           else 64 + ascii_value + 13 - 90)
            symbol = chr(ascii_value)
        elif 97 <= ascii_value <= 122:
            ascii_value = (ascii_value + 13
                           if ascii_value + 13 <= 122
                           else 96 + ascii_value + 13 - 122)
            symbol = chr(ascii_value)

        encoded_symbols.append(symbol)

    return ''.join(encoded_symbols)

# print(rot13('test'))
# print(rot13('Test'))
# print(rot13('aA bB zZ 1234 *!?%'))