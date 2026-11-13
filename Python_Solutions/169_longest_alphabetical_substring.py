def longest(st):
    longest_substring = ""
    current_substring = []

    for letter in st:
        if not current_substring or ord(current_substring[-1]) <= ord(letter):
            current_substring.append(letter)
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = "".join(current_substring)
            current_substring.clear()
            current_substring.append(letter)

    if current_substring and len(current_substring) > len(longest_substring):
        longest_substring = "".join(current_substring)

    return longest_substring


# print(longest("asd"))
# print(longest("nab"))
# print(longest("abcdeapbcdef"))
# print(longest("asdfaaaabbbbcttavvfffffdf"))
# print(longest("asdfbyfgiklag"))
# print(longest("z"))
# print(longest("zyba"))
