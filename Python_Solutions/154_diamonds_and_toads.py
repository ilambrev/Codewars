def diamonds_and_toads(sentence, fairy):
    if fairy == "good":
        points = {"r": 1, "R": 2, "c": 1, "C": 2}
        counts = {"ruby": 0, "crystal": 0}
        letter_map = {"r": "ruby", "R": "ruby", "c": "crystal", "C": "crystal"}
    else:
        points = {"p": 1, "P": 2, "s": 1, "S": 2}
        counts = {"python": 0, "squirrel": 0}
        letter_map = {"p": "python", "P": "python", "s": "squirrel", "S": "squirrel"}

    for letter in sentence:
        if letter in points:
            counts[letter_map[letter]] += points[letter]

    return counts


# print(diamonds_and_toads("Ruby and Crystal", "good"))
# print(diamonds_and_toads("This string contain some Ruby and some Crystal in it", "good"))
# print(diamonds_and_toads("Python and Squirrel", "evil"))
# print(diamonds_and_toads("This string contain some Python and some Squirrel in it", "evil"))
