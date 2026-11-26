import re


def string_transformer(s):
    reverse_s = s.swapcase()[::-1]
    pattern = r"[A-Za-z]+"
    matches = re.findall(pattern, reverse_s)

    for match in matches:
        pattern_to_replace = rf"\b{re.escape(match)}\b"
        reverse_s = re.sub(pattern_to_replace, match[::-1], reverse_s)

    return reverse_s


# print(string_transformer("Example string"))
# print(string_transformer("Example Input"))
# print(string_transformer("To be OR not to be That is the Question"))
# print(string_transformer(""))
# print(string_transformer("You Know When  THAT  Hotline Bling"))
# print(string_transformer(" A b C d E f G "))
