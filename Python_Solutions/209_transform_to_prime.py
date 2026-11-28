def is_prime(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def minimum_number(numbers):
    numbers_sum = sum(numbers)
    number = numbers_sum

    while True:
        if is_prime(number):
            return number - numbers_sum
        number += 1


# print(minimum_number([3, 1, 2]))
# print(minimum_number([5, 2]))
# print(minimum_number([1, 1, 1]))
# print(minimum_number([2, 12, 8, 4, 6]))
# print(minimum_number([50, 39, 49, 6, 17, 28]))
