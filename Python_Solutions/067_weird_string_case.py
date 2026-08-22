def transform_word(word):
    return "".join([word[i].upper() if i % 2 == 0 else word[i].lower() for i in range(len(word))])


def to_weird_case(words):
    return " ".join([transform_word(word) for word in words.split()])


# print(to_weird_case("This"))
# print(to_weird_case("is"))
# print(to_weird_case("THIs iS a TEST"))
