def number_of_pairs(gloves):
    colors = {}

    for color in gloves:
        colors[color] = colors.get(color, 0) + 1

    return sum(gloves // 2 for gloves in colors.values())


# print(number_of_pairs(["red", "red"]))
# print(number_of_pairs(["red", "green", "blue"]))
# print(number_of_pairs(["gray", "black", "purple", "purple", "gray", "black"]))
# print(number_of_pairs([]))
# print(number_of_pairs(["red", "green", "blue", "blue", "red", "green", "red", "red", "red"]))
