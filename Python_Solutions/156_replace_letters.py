def replace_letters(word):
    vowels_replacement = {"a": "z", "e": "d", "i": "h", "o": "n", "u": "t"}
    consonants_replacement = {"b": "e", "c": "e", "d": "e", "f": "i", "g": "i", "h": "i", "j": "o", "k": "o", "l": "o",
                            "m": "o", "n": "o", "p": "u", "q": "u", "r": "u", "s": "u", "t": "u", "v": "a", "w": "a",
                            "x": "a", "y": "a", "z": "a"}

    return "".join(vowels_replacement[letter] if letter in vowels_replacement else consonants_replacement[letter] for letter in word)


# print(replace_letters("cat"))
# print(replace_letters("codewars"))
# print(replace_letters("abcdtuvwxyz"))
