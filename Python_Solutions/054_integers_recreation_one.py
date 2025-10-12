from math import sqrt, floor

def list_squared(m, n):
    result = []

    for number in range(m, n + 1):
        end_of_range = floor(sqrt(number)) + 1
        divisors_sum = 1 if number == 1 else 1 + number ** 2

        for i in range(2, end_of_range):
            if number % i == 0:
                second_devisor = int(number / i)
                divisors_sum += i ** 2

                if i != second_devisor:
                    divisors_sum += second_devisor ** 2

        if sqrt(divisors_sum).is_integer():
            result.append([number, divisors_sum])

    return result

# print(list_squared(1, 250))
# print(list_squared(42, 250))
# print(list_squared(250, 500))