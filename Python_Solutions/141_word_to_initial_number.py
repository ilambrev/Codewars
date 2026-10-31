def convert(st):
    letters = list(dict.fromkeys(st.upper()))

    if len(letters) > 1:
        letters[0], letters[1] = letters[1], letters[0]

        return int("".join(str(letters.index(letter)) for letter in st.upper()))
    elif len(letters) == 1:
        return 1
    else:
        return 0


# print(convert("CodeWars"))
# print(convert("KATA"))
# print(convert("KaTA"))
