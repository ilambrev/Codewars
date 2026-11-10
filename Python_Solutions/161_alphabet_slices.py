def solution(s):
    result = []
    current_part = []

    for i in range(len(s)):
        current_char = s[i]

        if not current_part or ord(current_char) - ord(current_part[-1]) == 1:
            current_part.append(current_char)
        else:
            result += current_part[::-1]
            current_part.clear()
            current_part.append(current_char)

    if current_part:
        result += current_part[::-1]

    return "".join(result)


# print(solution("xabc"))
# print(solution("abcxdef"))
# print(solution("abcxyz"))
# print(solution("zahimzmstaz"))
# print(solution("jjjjjjjjklmnopqrstuv"))
# print(solution("zyx"))
# print(solution("ppqqrr"))
# print(solution("gjaababbboo"))
