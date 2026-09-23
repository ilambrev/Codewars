from string import ascii_lowercase


def is_isogram(word: str) -> bool:
    letters = {}

    for l in word:
        letter = l.lower()
        if letter in ascii_lowercase:
            letters[letter] = letters.get(letter, 0) + 1

    repeats = [r for r in letters.values()]

    different_repeats = [r for r in repeats if not r == repeats[0]]

    if letters and len(different_repeats) == 0:
        return True
    else:
        return False


# print(is_isogram("eeen"))
# print(is_isogram("isogram"))
# print(is_isogram("aba"))
# print(is_isogram("moOse"))
# print(is_isogram("isIsogram"))
