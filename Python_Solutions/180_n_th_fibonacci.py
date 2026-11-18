def nth_fib(n):
    fib = [0, 1]

    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    return fib[n-1]


# print(nth_fib(1))
# print(nth_fib(2))
# print(nth_fib(3))
# print(nth_fib(4))
# print(nth_fib(5))
# print(nth_fib(6))
# print(nth_fib(7))
