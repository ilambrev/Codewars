def string_expansion(s):
    output = []
    multiplier = 1

    if s and s[0].isalpha():
        output.append(s[0])

    for i in range(1, len(s)):
        if s[i].isalpha():
            if s[i-1].isnumeric():
                multiplier = int(s[i-1])

            output.append(multiplier * s[i])

    return "".join(output)


# print(string_expansion("3D2a5d2f"))
# print(string_expansion("4D1a8d4j3k"))
# print(string_expansion("4D2a8d4j2f"))
# print(string_expansion("3n6s7f3n"))
# print(string_expansion("0d4n8d2b"))
# print(string_expansion("0c3b1n7m"))
# print(string_expansion("7m3j4ik2a"))
# print(string_expansion("3A5m3B3Y"))
# print(string_expansion("5M0L8P1"))
# print(string_expansion("2B"))
# print(string_expansion("7M1n3K"))
# print(string_expansion("A4g1b4d"))


# print(string_expansion("111111"))
# print(string_expansion("4d324n2"))
# print(string_expansion("5919nf3u"))
# print(string_expansion("2n1k523n4i"))
# print(string_expansion("6o23M32d"))
# print(string_expansion("1B44n3r"))
# print(string_expansion("M21d1r32"))
# print(string_expansion("23M31r2r2"))
# print(string_expansion("8494mM25K2A"))
# print(string_expansion("4A46D6B3C"))
# print(string_expansion("23D42B3A"))
# print(string_expansion("143D36C1A"))


# print(string_expansion("asdf"))
# print(string_expansion("23jbjl1eb"))
# print(string_expansion("43ibadsr3"))
# print(string_expansion("123p9cdbjs"))
# print(string_expansion("2309ew7eh"))
# print(string_expansion("312987rfebd"))
# print(string_expansion("126cgec"))
# print(string_expansion("1chwq3rfb"))
# print(string_expansion("389fg21c"))
# print(string_expansion("239vbsac"))
# print(string_expansion("davhb327vuc"))
# print(string_expansion("cvyb239bved2dv"))


# print(string_expansion(""))
