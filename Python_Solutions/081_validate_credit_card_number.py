def validate(n):
    n_str = str(n)

    if n < 0 or len(n_str) > 16:
        return False

    digits = [int(d) for d in n_str]

    for i in range(len(digits) - 2, -1, -2):
        d = digits[i] * 2
        digits[i] = d if d <= 9 else d - 9

    return sum(digits) % 10 == 0

# print(validate(1714))
# print(validate(12345))
# print(validate(891))
# print(validate(123))
# print(validate(1))
# print(validate(2121))
# print(validate(1230))
