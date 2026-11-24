def twos_difference(lst):
    result = []

    lst.sort()
    i = 0

    while i < len(lst) - 1:
        if lst[i+1] - lst[i] == 2:
            result.append((lst[i], lst[i+1]))
        elif i + 2 < len(lst) and lst[i+2] - lst[i] == 2:
            result.append((lst[i], lst[i+2]))

        i += 1

    return result


# print(twos_difference([1, 2, 3, 4]))
# print(twos_difference([1, 3, 4, 6]))
# print(twos_difference([0, 3, 1, 4]))
# print(twos_difference([4, 1, 2, 3]))
# print(twos_difference([6, 3, 4, 1, 5]))
# print(twos_difference([3, 1, 6, 4]))
# print(twos_difference([1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56]))
# print(twos_difference([1, 4, 7, 10]))
# print(twos_difference([]))
