def solve(s):
    odd_substrings = []
    for i in range(1, len(s) + 1):
        for j in range(len(s) + 1 - i):
            current_substring = s[j:j+i]
            if not int(current_substring) % 2 == 0:
                odd_substrings.append(current_substring)

    return len(odd_substrings)


# print(solve("1347"))
# print(solve("1357"))
# print(solve("13471"))
# print(solve("134721"))
# print(solve("1347231"))
# print(solve("13472315"))
