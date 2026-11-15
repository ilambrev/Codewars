def solve(s):
    letters = {}

    for letter in s:
        letters[letter] = letters.get(letter, 0) + 1

    sorted_letters = list(sorted(letters.items(), key=lambda item: item[1], reverse=True))

    max_count = sorted_letters[0][1]

    if max_count == 1 or len(sorted_letters) == 1:
        return True

    if sum(0 if letter[1] != sorted_letters[0][1] else 1 for letter in sorted_letters[1:-1]) == len(sorted_letters[1:-1]) and sorted_letters[-1][1] == 1:
        return True

    for i in range(1, len(sorted_letters)):
        if max_count - sorted_letters[i][1] != 1:
            return False

    return True


# print(solve("aaaa"))
# print(solve("abba"))
# print(solve("abbba"))
# print(solve("aabbcc"))
# print(solve("aaaabb"))
# print(solve("aabbccddd"))
# print(solve("aabcde"))
# print(solve("abcde"))
# print(solve("aaabcde"))
# print(solve("abbccc"))
# print(solve("aabbccdddeee"))
