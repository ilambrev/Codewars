def solve(s):
    if s == s[::-1]:
        return "OK"

    for i in range(len(s)):
        current_s = s[:i] + s[i+1:]
        if current_s == current_s[::-1]:
            return "remove one"

    return "not possible"


# print(solve("abba"))
# print(solve("abbaa"))
# print(solve("abbaab"))
# print(solve("madmam"))
# print(solve("raydarm"))
# print(solve("hannah"))
