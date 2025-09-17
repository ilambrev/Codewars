def reverse_fizz_buzz(array):
    result = [0, 0]

    for i in range(len(array)):
        if isinstance(array[i], str):
            if 'Fizz' in array[i] and result[0] == 0:
                result[0] = i + 1
            if 'Buzz' in array[i] and result[1] == 0:
                result[1] = i + 1

        if not result[0] == 0 and not result[1] == 0:
            break

    return tuple(result)

# print(reverse_fizz_buzz([1, 2, 'Fizz', 4, 'Buzz']))
# print(reverse_fizz_buzz([1, 'Fizz', 'Buzz', 'Fizz', 5, 'FizzBuzz']))
# print(reverse_fizz_buzz([1, 'FizzBuzz', 3, 'FizzBuzz', 5, 'FizzBuzz']))
# print(reverse_fizz_buzz(['Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'FizzBuzz']))
# print(reverse_fizz_buzz([
#     1, 2, 3, 4, 5, 6, 7, 8, 'FizzBuzz', 10, 11, 12, 13, 14, 15, 16, 17, 'FizzBuzz',
#     19, 20, 21, 22, 23, 24, 25, 26, 'FizzBuzz', 28, 29, 30, 31, 32, 33, 34, 35,
#     'FizzBuzz', 37, 38, 39, 40, 41, 42, 43, 44, 'FizzBuzz', 46, 47, 48, 49, 50, 51,
#     52, 53, 'FizzBuzz', 55, 56, 57, 58, 59, 60, 61, 62, 'FizzBuzz', 64, 65, 66, 67,
#     68, 69, 70, 71, 'FizzBuzz', 73, 74, 75, 76, 77, 78, 79, 80, 'FizzBuzz', 82, 83,
#     84, 85, 86, 87, 88, 89, 'FizzBuzz', 91, 92, 93, 94, 95, 96, 97, 98, 'FizzBuzz'
# ]))