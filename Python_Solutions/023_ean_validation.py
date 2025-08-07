def validate_ean(code):
    digits = [int(digit) for digit in code]
    checksum_digit = digits[-1]
    digits_sum = 0

    for i in range(0, len(digits) - 1):
        if i % 2 == 0:
            digits_sum += digits[i]
        else:
            digits_sum += digits[i] * 3

    checksum = 0 if digits_sum % 10 == 0 else 10 - (digits_sum % 10)

    return checksum == checksum_digit

# print(validate_ean('4003301018398'))
# print(validate_ean('9783815820865'))
# print(validate_ean('9783815820864'))
# print(validate_ean('9783827317100'))