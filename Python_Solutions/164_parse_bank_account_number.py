def parse_bank_account(bank_account):
    digits_parts = [" _     _  _     _  _  _  _  _ ", "| |  | _| _||_||_ |_   ||_||_|", "|_|  ||_  _|  | _||_|  ||_| _|"]
    digits = {}

    for i in range(10):
        digit = []
        for j in range(3):
            digit.append(digits_parts[j][i*3:i*3+3])

        digits["".join(digit)] = i

    account_parts = bank_account[:-1].split("\n")

    account_digits = []

    for i in range(int(len(account_parts[0]) / 3)):
        digit = []
        for j in range(3):
            digit.append(account_parts[j][i*3:i*3+3])

        account_digits.append(str(digits["".join(digit)]))

    return int("".join(account_digits))


# bank_account = "    _  _     _  _  _  _  _ \n  | _| _||_||_ |_   ||_||_|\n  ||_  _|  | _||_|  ||_| _|\n"
# print(parse_bank_account(bank_account))

# bank_account = " _  _  _  _  _  _  _  _  _ \n| | _| _|| ||_ |_   ||_||_|\n|_||_  _||_| _||_|  ||_| _|\n"
# print(parse_bank_account(bank_account))

# bank_account = " _  _  _  _  _  _  _  _  _ \n|_| _| _||_||_ |_ |_||_||_|\n|_||_  _||_| _||_| _||_| _|\n"
# print(parse_bank_account(bank_account))
