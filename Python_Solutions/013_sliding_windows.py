def window(lngth, offst, lst):
    result = []
    range_start = 0

    if lngth == 0:
        range_start = -1

    for index in range(range_start, len(lst), offst):
        sub_list = lst[index:index + lngth]
        if len(sub_list) == lngth:
            result.append(sub_list)
    return result

# print(window(2, 1, [0, 1, 2, 3, 4]))
# print(window(2, 2, [0, 1, 2, 3, 4]))
# print(window(2, 3, [0, 1, 2, 3, 4]))
# print(window(3, 1, [0, 1, 2]))
# print(window(2, 1, [0, 1, 2]))
# print(window(1, 1, [0, 1, 2]))
# print(window(0, 1, [0, 1, 2]))