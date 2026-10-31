def check_vin(number):
    if len(number) != 17:
        return False

    number = number.upper()

    letters_to_numbers = {
        "A": "1",
        "B": "2",
        "C": "3",
        "D": "4",
        "E": "5",
        "F": "6",
        "G": "7",
        "H": "8",
        "I": None,
        "J": "1",
        "K": "2",
        "L": "3",
        "M": "4",
        "N": "5",
        "O": None,
        "P": "7",
        "Q": None,
        "R": "9",
        "S": "2",
        "T": "3",
        "U": "4",
        "V": "5",
        "W": "6",
        "X": "7",
        "Y": "8",
        "Z": "9"
    }
    invalid_characters = {"I", "O", "Q"}
    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]

    if not invalid_characters.isdisjoint(number):
        return False

    decoded_number = "".join(letters_to_numbers[symbol] if symbol in letters_to_numbers else symbol for symbol in number)

    product = sum(weights[index] * int(decoded_number[index]) for index in range(len(decoded_number)))

    mod_eleven = product % 11

    return number[8] == str(mod_eleven) if mod_eleven < 10 else number[8] == "X"


# print(check_vin("5YJ3E1EA7HF000337"))
# print(check_vin("5YJ3E1EAXHF000347"))
# print(check_vin("5VGYMVUX7JV764512"))
# print(check_vin("7WDMMTDV9TG739741"))
# print(check_vin("7JTRH08L5EJ234829"))
