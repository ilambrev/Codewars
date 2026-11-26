def format_words(words):
    if not words:
        return ""

    words = [word for word in words if word]

    if len(words) == 0:
        return ""
    if len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return " and ".join(words)
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]


# print(format_words(["one", "two", "three", "four"]))
# print(format_words(["one"]))
# print(format_words(["one", "", "three"]))
# print(format_words(["", "", "three"]))
# print(format_words(["one", "two", ""]))
# print(format_words([]))
# print(format_words(None))
# print(format_words([""]))
