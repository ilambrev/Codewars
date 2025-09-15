def fizz_buzz_custom(string_one='Fizz', string_two='Buzz', num_one=3, num_two=5):
    sequence = []

    for num in range(1, 100 + 1):
        if num % num_one == 0 and num % num_two == 0:
            sequence.append(f'{string_one}{string_two}')
        elif num % num_one == 0:
            sequence.append(string_one)
        elif num % num_two == 0:
            sequence.append(string_two)
        else:
            sequence.append(num)

    return sequence

# print(fizz_buzz_custom()[3])
# print(fizz_buzz_custom()[15])
# print(fizz_buzz_custom()[14])
# print(fizz_buzz_custom()[2])
# print(fizz_buzz_custom()[4])
# print(fizz_buzz_custom('Hey', 'There')[14])
# print(fizz_buzz_custom('Lol', 'Zor')[2])
# print(fizz_buzz_custom('Rainbow', 'Pony')[4])
# print(fizz_buzz_custom("What's ", "up?", 2, 7)[97])
# print(fizz_buzz_custom("Sixty", "Five", 6, 11)[65])
# print(fizz_buzz_custom("Happy", "Cow", 13, 27)[98])