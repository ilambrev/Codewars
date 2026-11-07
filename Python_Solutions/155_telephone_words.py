import itertools


def telephone_words(digit_string):
    nums_to_letters = {
        "1": "1",
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ",
        "0": "0"
    }
    raw_combinations = itertools.product(*[nums_to_letters[digit] for digit in digit_string])
    all_combinations = ["".join(combo) for combo in raw_combinations]

    return all_combinations


# print(telephone_words("0002"))
# print(telephone_words("1123"))
# print(telephone_words("1234"))
