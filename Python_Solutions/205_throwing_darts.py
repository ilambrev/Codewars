def score_throws(radii):
    points = 0
    counter = 0

    for r in radii:
        if r < 5:
            points += 10
            counter += 1
        elif 5 <= r <= 10:
            points += 5

    return points + 100 if radii and counter == len(radii) else points


# print(score_throws([1, 5, 11]))
# print(score_throws([15, 20, 30, 31, 32, 44, 100]))
# print(score_throws([1, 2, 3, 4]))
# print(score_throws([]))
# print(score_throws([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(score_throws([0, 5, 10, 10.5, 4.5]))
# print(score_throws([1]))
# print(score_throws([21, 10, 10]))
# print(score_throws([5, 5, 5, 5]))
# print(score_throws([4.9, 5.1]))
