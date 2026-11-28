def find_children(dancing_brigade):
    if dancing_brigade:
        letters = sorted(dancing_brigade.lower())
        current_letter = letters[0]
        letters[0] = letters[0].upper()

        for i in range(1, len(letters)):
            if letters[i] != current_letter:
                current_letter = letters[i]
                letters[i] = letters[i].upper()

        return "".join(letters)

    return dancing_brigade


# print(find_children("abBA"))
# print(find_children("AaaaaZazzz"))
# print(find_children("CbcBcbaA"))
# print(find_children("xXfuUuuF"))
# print(find_children(""))
