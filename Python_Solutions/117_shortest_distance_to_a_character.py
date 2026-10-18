def shortest_to_char(s, c):
    shortest_paths = []

    if s and c and c in s:
        for i in range(len(s)):
            left_index = s[:i+1][::-1].find(c)
            right_index = s[i:].find(c)

            if left_index > -1 and right_index > -1:
                shortest_paths.append(min(left_index, right_index))
            elif left_index > -1:
                shortest_paths.append(left_index)
            else:
                shortest_paths.append(right_index)

    return shortest_paths


# print(shortest_to_char("lovecodewars", "e"))
# print(shortest_to_char("aaaaa", "a"))
# print(shortest_to_char("aabbaabb", "a"))
# print(shortest_to_char("aaaabbbb", "b"))
# print(shortest_to_char("aaaaa", "b"))
# print(shortest_to_char("lovecoding", ""))
# print(shortest_to_char("", ""))
