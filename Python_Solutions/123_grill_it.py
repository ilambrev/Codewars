def grille(message, code):
    code_binary = format(code, f"0{len(message)}b")[::-1]
    reverse_message = message[::-1]

    return "".join([reverse_message[i] for i in range(len(reverse_message)) if code_binary[i] == "1"][::-1])


# print(grille("abcdef", 5))
# print(grille("", 5))
# print(grille("abcd", 1))
# print(grille("0abc", 2))
# print(grille("ab", 255))
# print(grille("ab", 256))
# print(grille("abcde", 32))
# print(grille("tcddoadepwweasresd", 77098))
