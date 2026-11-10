def split_digits_and_letter(str):
    digits = "0123456789"
    number = []
    letter = ""
    for symbol in str:
        if symbol in digits:
            number.append(symbol)
        else:
            letter = symbol

    return [int("".join(number)), letter]


def do_math(st):
    operations = [
        lambda a, b: a + b,
        lambda a, b: a - b,
        lambda a, b: a * b,
        lambda a, b: a / b
    ]
    numbers = [number[0] for number in sorted([split_digits_and_letter(part) for part in st.split()], key=lambda x: x[1])]

    result = numbers[0]

    for i in range(1, len(numbers)):
        operation_index = (i - 1) % len(operations)
        result = operations[operation_index](result, numbers[i])

    return round(result)


# print(do_math("24z6 1z23 y369 89z 900b"))
# print(do_math("24z6 1x23 y369 89a 900b"))
# print(do_math("10a 90x 14b 78u 45a 7b 34y"))
# print(do_math("111a 222c 444y 777u 999a 888p"))
# print(do_math("1z 2t 3q 5x 6u 8a 7b"))
