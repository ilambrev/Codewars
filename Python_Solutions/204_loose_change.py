def loose_change(cents):
    change_dict = {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0}

    if cents > 0:
        change_dict["Quarters"] = int(cents / 25)
        cents %= 25
        change_dict["Dimes"] = int(cents / 10)
        cents %= 10
        change_dict["Nickels"] = int(cents / 5)
        cents %= 5
        change_dict["Pennies"] = int(cents)

    return change_dict


# print(loose_change(29))
# print(loose_change(91))
# print(loose_change(0))
# print(loose_change(-2))
# print(loose_change(3.9))
