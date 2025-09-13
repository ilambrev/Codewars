from math import sqrt, floor

def solve(a, b):
    def is_number_prime(number):
        if number <= 1:
            return False

        for divisor in range(2, floor(sqrt(number)) + 1):
            if number % divisor == 0:
                return False

        return True

    def is_reduction_possible(number):
        tested_numbers = {number}

        while number > 1:
            digits = [int(digit) for digit in str(number)]
            current_number = sum([digit ** 2 for digit in digits])

            if current_number in tested_numbers:
                return False
            else:
                tested_numbers.add(current_number)

            number = current_number

        return True

    return len([num for num in range(a, b) if is_number_prime(num) and is_reduction_possible(num)])

# print(solve(1, 25))
# print(solve(100, 1000))
# print(solve(100, 2000))
# print(solve(100, 3000))
# print(solve(100, 4000))