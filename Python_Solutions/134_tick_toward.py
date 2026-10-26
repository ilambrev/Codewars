def tick_toward(start, target):
    x, y = start
    x_target, y_target = target
    x_diff = x_target - x
    y_diff = y_target - y
    x_factor = 1 if x_diff >= 0 else -1
    y_factor = 1 if y_diff >= 0 else -1
    medial_values = [(x, y)]

    for _ in range(max(abs(x_diff), abs(y_diff))):
        if x != x_target:
            x += x_factor

        if y != y_target:
            y += y_factor

        medial_values.append((x, y))

    return medial_values


# print(tick_toward((5, 5), (5, 7)))
# print(tick_toward((3, 2), (4, 5)))
# print(tick_toward((5, 1), (5, -2)))
