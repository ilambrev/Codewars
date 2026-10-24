def f(n: int, m: int) -> int:

    return int(int(n / m) * ((m - 1) * m) / 2 + ((n % m + 1) * (n % m)) / 2)


# print(f(10, 5))
# print(f(20, 20))
# print(f(15, 10))
