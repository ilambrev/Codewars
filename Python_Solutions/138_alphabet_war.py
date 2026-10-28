def alphabet_war(fight):
    left_side_letters = {
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1
    }
    right_side_letters = {
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1
    }
    left_side_score = 0
    right_side_score = 0

    for letter in fight:
        if letter in left_side_letters:
            left_side_score += left_side_letters[letter]
        elif letter in right_side_letters:
            right_side_score += right_side_letters[letter]

    result = "Let's fight again!"

    if left_side_score > right_side_score:
        result = "Left side wins!"
    elif right_side_score > left_side_score:
        result = "Right side wins!"

    return result


# print(alphabet_war("z"))
# print(alphabet_war("zdqmwpbs"))
# print(alphabet_war("wq"))
# print(alphabet_war("zzzzs"))
# print(alphabet_war("wwwwww"))
