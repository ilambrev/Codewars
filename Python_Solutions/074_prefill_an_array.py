def prefill(n, v=None) -> list:
    if isinstance(n, str) and n.isdigit():
        n = int(n)

    if not isinstance(n, bool) and isinstance(n, int) and n >= 0:
        return [v] * n
    else:
        raise TypeError(f"{str(n)} is invalid")


# print(prefill(3, 1))
# print(prefill(2, 'abc'))
# print(prefill('1', 1))
# print(prefill(3, prefill(2, '2d')))
# print(prefill('xyz', 1))
