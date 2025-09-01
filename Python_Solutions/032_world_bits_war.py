def bits_war(numbers):
    evens_result = 0
    odds_result = 0

    for num in numbers:
        num_binary_representation = format(num, 'b')
        ones_count = num_binary_representation.count('1')

        if num < 0:
            ones_count *= -1

        if num % 2 == 0:
            evens_result += ones_count
        else:
            odds_result += ones_count

    if evens_result > odds_result:
        return 'evens win'
    elif odds_result > evens_result:
        return 'odds win'
    else:
        return 'tie'

# print(bits_war([1, 5, 12]))
# print(bits_war([7, -3, 20]))
# print(bits_war([7, -3, -2, 6]))
# print(bits_war([-3, -5]))
# print(bits_war([]))