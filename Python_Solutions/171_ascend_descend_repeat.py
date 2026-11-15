def ascend_descend(length, minimum, maximum):
    if maximum < minimum or length == 0:
        return ""

    if minimum == maximum:
        return f"{minimum}" * length

    result = [str(minimum)]
    step = 1

    while len("".join(result)) < length:
        last_element = int(result[-1])

        if last_element == maximum and step == 1 or last_element == minimum and step == -1:
            step = -step

        result.append(str(int(last_element) + step))

    return "".join(result)[:length]


# print(ascend_descend(5, 1, 3))
# print(ascend_descend(14, 0, 2))
# print(ascend_descend(11, 5, 9))
