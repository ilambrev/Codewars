def decomp(n):
    def calculate_factorial(num: int):
        current_factorial = 1
        for i in range(1, num + 1):
            current_factorial *= i
        return current_factorial

    def is_prime(num: int):
        is_prime_num = True
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                is_prime_num = False
                break
        return is_prime_num

    def find_prime_factors(num: int):
        return [p for p in range(2, num + 1) if is_prime(p)]

    def factor_count(num: int, factor: int):
        counter = 0
        while True:
            if num % factor == 0:
                counter += 1
                num //= factor
            else:
                break
        return counter

    def format_output(factors_count: dict[int, int]):
        return " * ".join([f"{k}^{v}" if v > 1 else f"{k}" for k, v in factors_count.items()])

    factorial = calculate_factorial(n)
    prime_factors = find_prime_factors(n)
    prime_factors_count = {}

    for f in prime_factors:
        prime_factors_count[f] = prime_factors_count.get(f, 0) + factor_count(factorial, f)

    return format_output(prime_factors_count)

# print(decomp(5))
# print(decomp(14))
# print(decomp(17))
# print(decomp(22))
# print(decomp(25))
# print(decomp(79))
# print(decomp(3988))
# print(decomp(3989))
# print(decomp(3990))
