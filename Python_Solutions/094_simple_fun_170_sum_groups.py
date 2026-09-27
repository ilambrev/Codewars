def has_sequence(result):
    for i in range(1, len(result)):
        first = result[i-1] % 2 == 0
        second = result[i] % 2 == 0

        if first and second or (not first and not second):
            return True

    return False


def sum_groups(xs: list[int]) -> int:
    if len(xs) == 0:
        return 0

    result = [n for n in xs]

    while has_sequence(result):
        result_temp = []
        is_even = result[0] % 2 == 0
        temp_sum = result[0]

        for i in range(1, len(result)):
            current_n = result[i]
            current_n_type = current_n % 2 == 0
            if is_even and current_n_type or (not is_even and not current_n_type):
                temp_sum += current_n
            else:
                result_temp.append(temp_sum)
                temp_sum = current_n
                is_even = not is_even

        result_temp.append(temp_sum)

        result = [n for n in result_temp]

    return len(result)


# print(sum_groups([2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]))
# print(sum_groups([2, 1, 2, 2, 6, 5, 0, 2, 0, 3, 3, 3, 9, 2]))
# print(sum_groups([2]))
# print(sum_groups([1, 2]))
# print(sum_groups([1, 1, 2, 2]))
