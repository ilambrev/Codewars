def compute_depth(n):
    digits = set(str(n))
    counter = 1

    while len(digits) < 10:
        counter += 1
        digits.update(str(n * counter))

    return counter


# print(compute_depth(8))
# print(compute_depth(13))
# print(compute_depth(7))
# print(compute_depth(25))
# print(compute_depth(42))
# print(compute_depth(1))
