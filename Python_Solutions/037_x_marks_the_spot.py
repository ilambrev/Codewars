def x(n: int) -> list[list[int]]:
    result = [[0 for col in range(n)] for row in range(n)]

    for i in range(n):
        result[i][i] = 1

    for i in range(n - 1, -1, -1):
        result[n - i - 1][i] = 1

    return result

# print(x(1))
# print(x(2))
# print(x(3))
# print(x(4))
# print(x(5))
# print(x(6))