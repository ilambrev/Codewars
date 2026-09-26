def encrypt(text, rule):
    encrypted_text = [chr((ord(s) + rule) % 256) for s in text]

    return "".join(encrypted_text)


# print(encrypt("", 1))
# print(encrypt("a", 1))
# print(encrypt("please encrypt me", 2))
