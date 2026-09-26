def dashatize(n):
    digits = [d if int(d) % 2 == 0 else f'-{d}-' for d in str(abs(n))]
    result = "".join(digits)

    if result[0] == "-":
        result = result[1:]

    if result[-1] == "-":
        result = result[:-1]

    return result.replace("--", "-")


# print(dashatize(274))
# print(dashatize(5311))
# print(dashatize(86320))
# print(dashatize(974302))
# print(dashatize(0))
# print(dashatize(-1))
# print(dashatize(-28369))
