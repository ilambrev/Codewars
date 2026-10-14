def added_char(s1, s2):
    symbols = [s for s in s2]

    for s in s1:
        if s in symbols:
            symbols.pop(symbols.index(s))

    return symbols[0]


# print(added_char("hello", "checlclo"))
# print(added_char("aabbcc", "aacccbbcc"))
# print(added_char("abcde", "2db2a2ec"))
