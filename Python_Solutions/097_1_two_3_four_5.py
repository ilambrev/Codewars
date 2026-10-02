from math import ceil


def generate_pattern(digit_name, position, is_even):
    repeats = ceil(position / len(digit_name))
    pattern_parts = []

    if is_even:
        for i in range(repeats):
            if i % 2 == 0:
                pattern_parts.append(digit_name)
            else:
                pattern_parts.append(digit_name.upper())
    else:
        for i in range(repeats):
            if i % 2 == 0:
                pattern_parts.append(digit_name.upper())
            else:
                pattern_parts.append(digit_name)

    return "".join(pattern_parts)[:position]


def convert_even_length_number(num_digits, digits_names):
    converted_digits = []

    for i in range(len(num_digits)):
        digit = num_digits[i]
        digit_name = digits_names[digit]
        position = i + 1

        if int(digit) % 2 == 0:
            converted_digits.append(
                generate_pattern(digit_name, position, True))
        else:
            converted_digits.append(digit)

    return "".join(converted_digits)


def convert_odd_length_number(num_digits, digits_names):
    converted_digits = []

    for i in range(len(num_digits)):
        digit = num_digits[i]
        digit_name = digits_names[digit]
        position = i + 1

        if not int(digit) % 2 == 0:
            converted_digits.append(generate_pattern(digit_name, position, False))
        else:
            converted_digits.append(digit)

    return "".join(converted_digits)


def conv(num):
    digits_names = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    num_digits = [d for d in str(num)]
    num_length = len(num_digits)

    if num_length % 2 == 0:
        return "".join(convert_even_length_number(num_digits, digits_names))
    else:
        return "".join(convert_odd_length_number(num_digits, digits_names))


# print(conv(0))
# print(conv(11))
# print(conv(1101))
# print(conv(54563))
# print(conv(47309534))
# print(conv(34266262106))
# print(conv(15795379351687))
# print(conv(157953793516872))
