def highest_rank(arr):
    numbers_repeats = {}
    for num in arr:
        numbers_repeats[num] = numbers_repeats.get(num, 0) + 1

    return [k for k, _ in sorted(numbers_repeats.items(), key=lambda el: (el[1], el[0]), reverse=True)][0]


# print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
# print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))
# print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))
# print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]))
# print(highest_rank([1, 2, 3]))
# print(highest_rank([1, 1, 2, 3]))
# print(highest_rank([1, 1, 2, 2, 3]))
