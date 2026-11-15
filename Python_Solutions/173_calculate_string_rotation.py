def shifted_diff(first, second):
    if len(first) != len(second):
        return -1

    for i in range(len(second)):
        if first == second:
            return i

        first = first[-1] + first[:-1]

    return -1


# print(shifted_diff("eecoff", "coffee"))
# print(shifted_diff("Moose", "moose"))
# print(shifted_diff("isn't", "'tisn"))
# print(shifted_diff("Esham", "Esham"))
# print(shifted_diff(" ", " "))
# print(shifted_diff("hoop", "pooh"))
# print(shifted_diff("  ", " "))
