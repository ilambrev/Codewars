def bears(x, s):
    bears = ["B8", "8B"]
    result = []
    index = 0

    while index < len(s) - 1:
        str_part = s[index:index+2]
        if str_part in bears:
            result.append(str_part)
            index += 2
        else:
            index += 1

    result = "".join(result)

    return [result, len(result) >= x]


# print(bears(7, "8j8mBliB8gimjB8B8jlB"))
# print(bears(3, "88Bifk8hB8BB8BBBB888chl8BhBfd"))
# print(bears(8, "8"))
# print(bears(1, "j8BmB88B88gkBBlf8hg8888lbe88"))
# print(bears(0, "8j888aam"))
