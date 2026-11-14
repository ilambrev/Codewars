def is_enum_list_valid(enum_list):
    if not isinstance(enum_list, list):
        return False

    indexes = []

    for element in enum_list:
        if not isinstance(element, tuple):
            return False

        if len(element) > 2:
            return False

        if not str(element[0]).isnumeric():
            return False

        if not isinstance(element[0], int):
            return False

        if len(str(element[1])) > 1:
            return False

        if not str(element[1]).isalnum():
            return False

        indexes.append(element[0])

    indexes.sort()

    return indexes[0] == 0 and indexes[-1] == len(indexes) - 1


def denumerate(enum_list):
    is_input_valid = is_enum_list_valid(enum_list)

    if not is_input_valid:
        return False
    else:
        return "".join(element[1] for element in sorted(enum_list))


# print(denumerate([(4, 'y'), (1, 'o'), (3, 't'), (0, 'm'), (2, 'n')]))
# print(denumerate([(1, '3'), (2, 'l'), (4, 'o'), (3, 'l'), (0, 'h')]))
# print(denumerate([(0, '%')]))
# print(denumerate([(1, 'a'), (2, 'b')]))
