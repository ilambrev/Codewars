def is_prime_happy(n):
    if n < 4:
        return False

    primes = []

    for i in range(n - 1, 1, -1):
        is_prime = True

        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

    return len(primes) > 0 and sum(primes) % n == 0


# print(is_prime_happy(5))
# print(is_prime_happy(8))
# print(is_prime_happy(25))
# print(is_prime_happy(32))
# print(is_prime_happy(2))
# print(is_prime_happy(0))
