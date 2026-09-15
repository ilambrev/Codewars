def good_vs_evil(good, evil):
    good_races_worth = [1, 2, 3, 3, 4, 10]
    evil_races_worth = [1, 2, 2, 2, 3, 5, 10]
    good = [int(d) for d in good.split()]
    evil = [int(d) for d in evil.split()]

    good_worth_sum = sum([good_races_worth[i] * good[i] for i in range(len(good_races_worth))])
    evil_worth_sum = sum([evil_races_worth[i] * evil[i] for i in range(len(evil_races_worth))])

    if good_worth_sum > evil_worth_sum:
        return "Battle Result: Good triumphs over Evil"
    elif evil_worth_sum > good_worth_sum:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

# print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
# print(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))
# print(good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))
