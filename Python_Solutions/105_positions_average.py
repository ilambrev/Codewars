def find_matches(s1, s2):
    return len([i for i in range(len(s1)) if s1[i] == s2[i]])


def pos_average(s):
    strings = s.split(", ")
    combinations_count = len(strings) * ((len(strings) - 1)) / 2
    positions_count = combinations_count * len(strings[0])
    position_matches = 0

    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            position_matches += find_matches(strings[i], strings[j])

    return 100 * (position_matches / positions_count) if position_matches > 0 else 0


# print(pos_average("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"))
# print(pos_average("444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"))
# print(pos_average("449404, 099090, 600999, 694460, 996066, 906406, 644994, 699094, 064990, 696046"))
# print(pos_average("660999, 969060, 044604, 009494, 609009, 640090, 994446, 949940, 046999, 609444"))
# print(pos_average("996060, 606494, 964494, 460409, 609449, 969600, 960944, 960006, 666049, 090996"))
# print(pos_average("40664064, 60460960, 00669664, 94040464, 04006499, 00466666, 90966460, 64494990"))
# print(pos_average("64040600, 64464440, 60006040, 49609906, 46664409, 99464446, 90446964, 96940090"))
# print(pos_average("99494909, 60004094, 60090496, 64664669, 49909604, 49999064, 46009964, 44494444"))
# print(pos_average("46904946, 60996660, 64040460, 40449469, 46440460, 96090699, 06600440, 44046966"))
# print(pos_average("46099969, 64096999, 44949949, 06409969, 09064604, 90490494, 04600696, 94469969"))
# print(pos_average("4444444, 4444444, 4444444, 4444444, 4444444, 4444444, 4444444, 4444444"))
# print(pos_average("0, 0, 0, 0, 0, 0, 0, 0"))
# print(pos_average("0, 0, 1"))
