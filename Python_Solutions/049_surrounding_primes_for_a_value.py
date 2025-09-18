from math import floor, sqrt

def prime_bef_aft(num):
    result = []

    for number in range(num - 1, 2, -1):
        for divisor in range(2, floor(sqrt(number)) + 1):
            if number % divisor == 0:
                break

        else:
            result.append(number)
            break

    number = num + 1

    while len(result) < 2:
        for divisor in range(2, floor(sqrt(number)) + 1):
            if number % divisor == 0:
                break

        else:
            result.append(number)
            break

        number += 1

    return result

# print(prime_bef_aft(100))
# print(prime_bef_aft(97))
# print(prime_bef_aft(101))
# print(prime_bef_aft(120))
# print(prime_bef_aft(130))