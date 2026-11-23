def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None

    squares_sizes = []

    while lng > 0 and wdth > 0:
        if lng > wdth:
            squares_sizes.append(wdth)
            lng -= wdth
        elif lng < wdth:
            squares_sizes.append(lng)
            wdth -= lng
        else:
            squares_sizes.append(lng)
            lng -= wdth
            wdth -= lng

    return squares_sizes


# print(sq_in_rect(5, 5))
# print(sq_in_rect(5, 3))
# print(sq_in_rect(3, 5))
# print(sq_in_rect(20, 14))
