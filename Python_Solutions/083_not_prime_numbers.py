def are_all_prime_digits(num):
    prime_digits = ["2", "3", "5", "7"]
    num_str = str(num)

    for d in num_str:
        if d not in prime_digits:
            return False

    return True


def is_not_prime_number(num):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return True

    return False


def not_primes(a, b):
    return [n for n in range(a, b) if are_all_prime_digits(n) and is_not_prime_number(n)]

# print(not_primes(2, 222))
# print(not_primes(2, 77))
# print(not_primes(2700, 3000))
# print(not_primes(500, 999))
# print(not_primes(999, 2500))
