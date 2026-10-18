from string import ascii_uppercase


def insert_missing_letters(st):
    available_letters = set(st)
    letters_appeared_once = []
    result = []

    for l in st:
        result.append(l)

        if l not in letters_appeared_once and not l == "z":
            letters_appeared_once.append(l)
            next_letter = chr(ord(l) + 1)
            index = ascii_uppercase.find(next_letter.upper())
            result.append("".join([letter for letter in ascii_uppercase[index:] if not letter.lower() in available_letters]))

    return "".join(result)


# print(insert_missing_letters("hello"))
# print(insert_missing_letters("abcdefghijklmnopqrstuvwxyz"))
# print(insert_missing_letters("hellllllllllllooooo"))
# print(insert_missing_letters("pixxa"))
# print(insert_missing_letters("xpixax"))
# print(insert_missing_letters("z"))
