def sum_consecutives(lst):
    result = [lst[0]] if lst else []

    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            result[-1] += lst[i]
        else:
            result.append(lst[i])

    return result


# print(sum_consecutives([1, 4, 4, 4, 0, 4, 3, 3, 1]))
# print(sum_consecutives([1, 1, 7, 7, 3]))
# print(sum_consecutives([-5, -5, 7, 7, 12, 0]))
# print(sum_consecutives([3, 3, 3, 3, 1]))
# print(sum_consecutives([2, 2, -4, 4, 5, 5, 6, 6, 6, 6, 6, 1]))
# print(sum_consecutives([1, 1, 1, 1, 1, 3]))
# print(sum_consecutives([1, -1, -2, 2, 3, -3, 4, -4]))
# print(sum_consecutives([0, 1, 1, 2, 2]))
