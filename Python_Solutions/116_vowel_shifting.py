def vowel_shift(text, n):
    if not text or n == 0:
        return text

    vowels = "AEIOUaeiou"
    vowels_in_text = [s for s in text if s in vowels]

    if not vowels_in_text:
        return text

    rotation = abs(n) % len(vowels_in_text)

    if n > 0:
        vowels_in_text = vowels_in_text[-rotation:] + vowels_in_text[:-rotation]

    if n < 0:
        vowels_in_text = vowels_in_text[rotation:] + vowels_in_text[:rotation]

    i = 0
    result = []

    for symbol in text:
        if symbol in vowels:
            result.append(vowels_in_text[i])
            i += 1
        else:
            result.append(symbol)

    return "".join(result)


# print(vowel_shift(None, 0))
# print(vowel_shift("", 0))
# print(vowel_shift("This is a test!", 0))
# print(vowel_shift("This is a test!", 1))
# print(vowel_shift("This is a test!", 3))
# print(vowel_shift("This is a test!", 4))
# print(vowel_shift("This is a test!", -1))
# print(vowel_shift("This is a test!", -5))
# print(vowel_shift("Brrrr", 99))
# print(vowel_shift("AEIOUaeiou", 1))
