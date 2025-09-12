def solve(st, idx):
    closing_bracket_index = -1
    opening_brackets_count = 0
    closing_bracket_count = 0

    if st[idx] == '(':
        for i in range(idx, len(st)):
            if st[i] == '(':
                opening_brackets_count += 1

            if st[i] == ')':
                closing_bracket_count += 1

            if opening_brackets_count > 0 and opening_brackets_count == closing_bracket_count:
                closing_bracket_index = i
                break

    return closing_bracket_index

# print(solve("((1)23(45))(aB)", 0))
# print(solve("((1)23(45))(aB)", 1))
# print(solve("((1)23(45))(aB)", 2))
# print(solve("((1)23(45))(aB)", 6))
# print(solve("((1)23(45))(aB)", 11))
# print(solve("((>)|?(*'))(yZ)", 11))
# print(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))", 11))
# print(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))", 0))
# print(solve("(>_(va)`?(h)C(as)(x(hD)P|(fg)))", 19))