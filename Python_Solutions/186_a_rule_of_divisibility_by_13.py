def thirt(n):
    remainders = [1, 10, 9, 12, 3, 4]

    while True:
        digits = [int(d) for d in str(n)][::-1]
        new_n = sum(digits[i] * remainders[i % len(remainders)] for i in range(len(digits)))
        if new_n == n:
            return n
        else:
            n = new_n


# print(thirt(8529))
# print(thirt(85299258))
# print(thirt(5634))
# print(thirt(1111111111))
# print(thirt(987654321))
