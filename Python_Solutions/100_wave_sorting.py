def wave_sort(xs: list[int]) -> None:
    xs.sort(reverse=True)
    elements_count = len(xs)

    for i in range(1, int(elements_count / 2) + 1):
        xs.insert(i * 2 - 1, xs.pop(-1))

    return

    # return xs


# print(wave_sort([]))
# print(wave_sort([1]))
# print(wave_sort([1, 2]))
# print(wave_sort([2, 1]))
# print(wave_sort([1, 1, 1, 1]))
# print(wave_sort([1, 2, 3]))
# print(wave_sort([1, 3, 2]))
# print(wave_sort([2, 1, 3]))
# print(wave_sort([2, 3, 1]))
# print(wave_sort([3, 1, 2]))
# print(wave_sort([3, 2, 1]))
# print(wave_sort([1, 2, 34, 4, 5, 5, 5, 65, 6, 65, 5454, 4]))
