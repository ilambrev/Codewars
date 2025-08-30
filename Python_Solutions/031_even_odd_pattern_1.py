def even_odd(arr):
    result = arr[0]

    for i in range(1, len(arr)):
        if i % 2 != 0:
            result *= arr[i]
        else:
            result += arr[i]

    return result

# print(even_odd([1, 2, 6, 1, 6, 3, 1, 9, 6]))
# print(even_odd([1, 2, 6, 1, 6, 1, 3, 9, 6]))
# print(even_odd([1, 2, 2, 1, 6, 1, 3, 9, 6, 1]))
# print(even_odd([1, 2, 3]))
# print(even_odd([0, 2, 3]))
# print(even_odd([1, 0, 3]))
# print(even_odd([0, 0, 3]))
# print(even_odd([3, 0]))
# print(even_odd([1, 2, 2, 1, 6, 1, 3, 9, 6, 2, 32]))
# print(even_odd([1, 2, 2, 1, 6, 10, 3, -1, 6, 2, 32]))