def vowel_back(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    result = []

    for letter in st:
        move = 9
        index = alphabet.index(letter)

        if letter in "co":
            move = -1
        elif letter == "d":
            move = -3
        elif letter == "e":
            move = -4
        elif letter in vowels:
            move = -5

        index = (move + index) % len(alphabet)

        if alphabet[index] in "code":
            result.append(letter)
        else:
            result.append(alphabet[index])

    return "".join(result)


# print(vowel_back("testcase"))
# print(vowel_back("codewars"))
# print(vowel_back("exampletesthere"))
