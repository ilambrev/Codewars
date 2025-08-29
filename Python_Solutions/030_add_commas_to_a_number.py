def commas(num):
    if isinstance(num, float):
        num_as_str = str(round(num, 3))
    else:
        num_as_str = str(num)

    number_parts = num_as_str.split('.')
    is_num_with_more_than_three_digits = len(number_parts[0]) > 3
    is_num_negative = number_parts[0][0] == '-'

    if is_num_negative:
        number_parts[0] = number_parts[0][1:]

    if len(number_parts) > 1 and int(number_parts[1]) == 0:
        num_as_str = number_parts[0]
        number_parts.pop()

    if is_num_with_more_than_three_digits:
        integer_parts = []

        begin_index = len(number_parts[0]) % 3

        if begin_index > 0:
            integer_parts.append(number_parts[0][:begin_index])

        for i in range(begin_index, len(number_parts[0]), 3):
            integer_parts.append(number_parts[0][i:i + 3])

        result = ','.join(integer_parts)

        if is_num_negative:
            result = '-' + result

        if len(number_parts) > 1:
            result += f'.{number_parts[1]}'

        return result
    else:
        return num_as_str

# print(commas(1))
# print(commas(1000))
# print(commas(100.2346))
# print(commas(1000000000.23))
# print(commas(9123.212))
# print(commas(-1))
# print(commas(-1000000.123))
# print(commas(-2000.0))
# print(commas(-999.9999))
# print(commas(-1234567.0001236))
# print(commas(-305.329))