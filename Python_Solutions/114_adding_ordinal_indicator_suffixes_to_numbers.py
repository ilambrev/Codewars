def number_to_ordinal(n: int) -> str:
    suffixes = {
        "0": "",
        "1": "st",
        "2": "nd",
        "3": "rd",
    }
    n_str = str(n)
    result = ""

    if 0 <= n < 4:
        result = f"{n}{suffixes[n_str]}"
    elif n > 9:
        last_two_digits = int(n_str[-2:])
        if 9 < last_two_digits < 20:
            result = f"{n}th"
        else:
            last_digit = n_str[-1]
            if 0 < int(last_digit) < 4:
                result = f"{n}{suffixes[last_digit]}"
            else:
                result = f"{n}th"
    else:
        result = f"{n}th"

    return result


# print(number_to_ordinal(1))
# print(number_to_ordinal(2))
# print(number_to_ordinal(3))
# print(number_to_ordinal(4))
