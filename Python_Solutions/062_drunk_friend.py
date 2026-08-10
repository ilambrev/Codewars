def decode(string_):
    if not type(string_) == str:
        return "Input is not a string"

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []

    for l in string_:
        is_upper = l.isupper()
        l = l.lower()

        if l in alphabet:
            index = alphabet.find(l)
            l = alphabet[24 + 1 - index]

        if is_upper:
            l = l.upper()

        result.append(l)

    return "".join(result)

# print(decode("yvvi"))
# print(decode("Blf zoivzwb szw 10 yvvih"))
# print(decode("Ovg'h hdrn rm gsv ulfmgzrm!"))
# print(decode({"brand": "Starobrno" }))
# print(decode("Tl slnv, blf'iv wifmp"))
# print(decode("Hfiv r xzm wzmxv lm xlk'h xzi, slow nb yvvi"))
# print(decode(True))
# print(decode("Hvv? R'n mlg gszg wifmp, r xzm hgroo gzpv nb xolgsvh luu"))
# print(decode(123))
# print(decode(["Beer"]))