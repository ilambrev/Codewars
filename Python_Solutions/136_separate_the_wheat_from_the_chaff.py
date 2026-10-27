def wheat_from_chaff(values):
    end_index = len(values) - 1

    for i in range(len(values)):
        if values[i] >= 0:

            for j in range(end_index, i, -1):
                if values[j] < 0:
                    values[i], values[j] = values[j], values[i]
                    end_index = j
                    break

    return values


# print(wheat_from_chaff([2, -4, 6, -6]))
# print(wheat_from_chaff([7, -3, -10]))
# print(wheat_from_chaff([7, -8, 1, -2]))
# print(wheat_from_chaff([8, 10, -6, -7, 9]))
# print(wheat_from_chaff([-3, 4, -10, 2, -6]))
# print(wheat_from_chaff([2, -6, -4, 1, -8, -2]))
# print(wheat_from_chaff([16, 25, -48, -47, -37, 41, -2]))
# print(wheat_from_chaff([-30, -11, 36, 38, 34, -5, -50]))
# print(wheat_from_chaff([-31, -5, 11, -42, -22, -46, -4, -28]))
# print(wheat_from_chaff([46, 39, -45, -2, -5, -6, -17, -32, 17]))
# print(wheat_from_chaff([-9, -8, -6, -46, 1, -19, 44]))
# print(wheat_from_chaff([-37, -10, -42, 19, -31, -40, -45, 33]))
# print(wheat_from_chaff([-25, -48, -29, -25, 1, 49, -32, -19, -46, 1]))
# print(wheat_from_chaff([-7, -35, -46, -22, 46, 43, -44, -14, 34, -5, -26]))
# print(wheat_from_chaff([-46, -50, -28, -45, -27, -40, 10, 35, 34, 47, -46, -24]))
# print(wheat_from_chaff([-33, -14, 16, 31, 4, 41, -10, -3, -21, -12, -45, 41, -19]))
# print(wheat_from_chaff([-17, 7, -12, 10, 4, -8, -19, -24, 40, 31, -29, 21, -45, 1]))
# print(wheat_from_chaff([-16, 44, -7, -31, 9, -43, -44, -18, 50, 39, -46, -24, 3, -34, -27]))
