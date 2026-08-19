def encode(st):
    symbols = []
    symbol = st[0]
    counter = 1

    for i in range(1, len(st)):
        current_symbol = st[i]
        if current_symbol == symbol:
            counter += 1
        else:
            symbols.append(f"{counter}{symbol}")
            counter = 1
            symbol = current_symbol

    symbols.append(f"{counter}{symbol}")

    return "".join(symbols)


def decode(st):
    symbols = []
    number = st[0]

    for i in range(1, len(st)):
        current_symbol = st[i]
        if current_symbol.isdigit():
            number += current_symbol
        else:
            symbols.append(current_symbol * int(number))
            number = ""

    return "".join(symbols)


# print(encode("A"))
# print(encode("AAA"))
# print(encode("AB"))
# print(encode("AAABBBCCCA"))

# print(decode("1A"))
# print(decode("3A"))
# print(decode("1A1B"))
# print(decode("3A3B3C1A"))

# print(encode(decode("10A1B")))
# print(encode(decode("1A1B1C1D1E1F1G1H1I1J1K1L1M1N1O1P1Q1R1S1T1U1V1W1X1Y1Z")))
# print(decode(encode("AAAAAAAAAAB")))
# print(decode(encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ")))
