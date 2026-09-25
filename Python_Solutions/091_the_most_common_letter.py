from string import ascii_lowercase


def replace_common(st, letter):
    letters = {}

    for s in st:
        if s in ascii_lowercase:
            letters[s] = letters.get(s, 0) + 1

    most_common_letter = [k for k, _ in (sorted(letters.items(), key=lambda item: item[1], reverse=True))][0]

    return st.replace(most_common_letter, letter)


# print(replace_common("my mom loves me as never did", "t"))
# print(replace_common("real talk bro", "n"))
# print(replace_common("great job go ahead", "k"))
# print(replace_common("yyyaaa twwww ttt uuu ccca", "p"))
