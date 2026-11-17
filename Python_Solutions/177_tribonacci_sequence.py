def tribonacci(signature, n):
    for i in range(n - 3):
        signature.append(sum(signature[i:i+3]))

    return signature[:n]


# print(tribonacci([1, 1, 1], 10))
# print(tribonacci([0, 0, 1], 10))
# print(tribonacci([0, 1, 1], 10))
# print(tribonacci([1, 0, 0], 10))
# print(tribonacci([0, 0, 0], 10))
# print(tribonacci([1, 2, 3], 10))
# print(tribonacci([3, 2, 1], 10))
# print(tribonacci([1, 1, 1], 1))
# print(tribonacci([300, 200, 100], 0))
# print(tribonacci([0.5, 0.5, 0.5], 30))
