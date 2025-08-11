def solve(st, k):
    result = list(st)

    for code in range(97, 123):
        current_result_state = ''.join(result)
        result.clear()
        current_letter = chr(code)

        for letter in current_result_state:
            if letter == current_letter and k > 0:
                k -= 1
            else:
                result.append(letter)

        if k == 0:
            break

    return ''.join(result)

# print(solve('abracadabra', 1))
# print(solve('abracadabra', 2))
# print(solve('abracadabra', 6))
# print(solve('abracadabra', 8))
# print(solve('abracadabra', 50))
# print(solve('hxehmvkybeklnj', 5))
# print(solve('cccaabababaccbc', 3))
# print(solve('cccaabababaccbc', 9))
# print(solve('u', 1))
# print(solve('back', 3))