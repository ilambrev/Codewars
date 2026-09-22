def get_letters_in_st(st):
    letters = {}

    for letter in st:
        letters[letter] = letters.get(letter, 0) + 1

    return letters


def count_feelings(st, arr):
    counter = 0

    for feeling in arr:
        letters = get_letters_in_st(st)
        is_feeling_in_string = True

        for letter in feeling:
            if letter in letters and letters[letter] > 0:
                letters[letter] -= 1
            else:
                is_feeling_in_string = False
                break

        if is_feeling_in_string:
            counter += 1

    return f"{counter} {'feeling' if counter == 1 else 'feelings'}."


# print(count_feelings("longi", ["anger", "awe", "joy", "longing", "grief"]))
# print(count_feelings("yliausoenvjw", ["anger", "awe", "joy", "love", "grief"]))
# print(count_feelings("angerw", ["anger", "awe", "joy", "love", "grief"]))
# print(count_feelings("griefgriefgrief", ["anger", "awe", "joy", "love", "grief"]))
# print(count_feelings("abcdkasdfvkadf", ["desire", "joy", "shame", "longing", "fear"]))
