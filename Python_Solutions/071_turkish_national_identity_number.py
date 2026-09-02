def check_valid_tr_number(number):
    number_str = str(number)

    first_rule = number_str.isdigit() and len(number_str) == 11 and not number_str[0] == "0"

    if first_rule:
        digits = [int(d) for d in number_str]
        first_sum = sum([digits[0], digits[2], digits[4], digits[6], digits[8]])
        second_sum = sum([digits[1], digits[3], digits[5], digits[7]])

        second_rule = (first_sum * 7 - second_sum) % 10 == digits[9]

        if second_rule:
            third_rule = sum(digits[:-1]) % 10 == digits[10]

            return third_rule

    return False


# print(check_valid_tr_number(6923522112))
# print(check_valid_tr_number(692352217312))
# print(check_valid_tr_number("x5810a78432"))
# print(check_valid_tr_number(36637640050))
# print(check_valid_tr_number(12762438338))