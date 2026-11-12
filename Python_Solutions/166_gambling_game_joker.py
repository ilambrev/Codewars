def joker_card(joker_nums, ticket_serials):
    ticket_digits = 6
    prizes = {
        0: "Losing card",
        1: "Losing card",
        2: "V type",
        3: "IV type",
        4: "III type",
        5: "II type",
        6: "I type"
    }
    winning_combination = "".join(str(num)[-1] for num in joker_nums)
    results = []
    last_digits = ticket_digits

    for serial in ticket_serials:
        for i in range(ticket_digits):
            if serial[i:] == winning_combination[i:]:
                break
            else:
                last_digits -= 1

        results.append(prizes[last_digits])
        last_digits = ticket_digits

    return results


# print(joker_card([12, 35, 1, 2, 23, 39], ["151239", "251229", "251339"]))
# print(joker_card([5, 45, 35, 25, 15, 1], ["555551", "235551", "555552"]))
# print(joker_card([2, 17, 33, 12, 39, 44], ["000022", "001194", "232294"]))
# print(joker_card([20, 30, 40, 1, 2, 3], ["000123", "000125", "520123"]))
