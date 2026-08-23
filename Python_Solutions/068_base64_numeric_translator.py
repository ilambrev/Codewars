def base64_to_base10(s):
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    number = 0
    power = 0
    base = 64

    for digit in s[::-1]:
        value = digits.find(digit)
        number += value * base ** power
        power += 1

    return number


# print(base64_to_base10("A"))
# print(base64_to_base10("/"))
# print(base64_to_base10("BA"))
# print(base64_to_base10("//"))
# print(base64_to_base10("WIN"))
