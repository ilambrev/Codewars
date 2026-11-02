def reverse_vowels(s):
    vowels = "aeiou"
    vowels_in_s = "".join(symbol for symbol in s if symbol.lower() in vowels)
    reverse_vowels_in_s = vowels_in_s[::-1]
    result = []
    index = 0

    for symbol in s:
        if symbol in vowels_in_s:
            result.append(reverse_vowels_in_s[index])
            index += 1
        else:
            result.append(symbol)

    return "".join(result)


# print(reverse_vowels("Hello!"))
# print(reverse_vowels("Tomatoes"))
# print(reverse_vowels("Reverse Vowels In A String"))
