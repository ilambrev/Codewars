def solved(s):
    if not len(s) % 2 == 0:
        half = int(len(s) / 2)
        s = s[:half] + s[half + 1:]
    return "".join(sorted([symbol for symbol in s]))

# print(solved("Hello World"))
# print(solved("foobar"))
# print(solved("I see what you did there!"))
# print(solved(""))
# print(solved("abcd"))
# print(solved("abcde"))