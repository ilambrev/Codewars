def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None

    result = []
    for i in range(1, n + 1, 2):
        result.append(" " * int((n - i) / 2) + "*" * i + "\n")

    return "".join(result + result[-2::-1])

# print(diamond(1))
# print(diamond(2))
# print(diamond(3))
# print(diamond(5))
# print(diamond(0))
# print(diamond(-3))
