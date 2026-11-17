def find_missing(sequence):
    return (sequence[0] + sequence[-1]) * (len(sequence) + 1) // 2 - sum(sequence)


# print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
# print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))
