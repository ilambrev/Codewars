def series_slices(digits, n):
    if n <= len(digits):
        return [[int(d) for d in digits[i:i+n]] for i in range(len(digits) - n + 1)]
    else:
        raise Exception("n is larger than the length of the string")


# print(series_slices("01234", 2))
# print(series_slices("01234", 4))
# print(series_slices("01234", 6))
