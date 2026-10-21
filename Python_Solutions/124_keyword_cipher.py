from string import ascii_lowercase


def generate_encryption_key(keyword):
    non_repeated_letters = []
    not_used_letters = []

    for l in keyword:
        if not l in non_repeated_letters:
            non_repeated_letters.append(l)

    for l in ascii_lowercase:
        if not l in non_repeated_letters:
            not_used_letters.append(l)

    return "".join(non_repeated_letters) + "".join(not_used_letters)


def encrypt_msg(msg, encryption_key):
    msg = msg.lower()
    encrypted_word_letters = []

    for l in msg:
        if l in ascii_lowercase:
            index = ascii_lowercase.index(l)
            encrypted_word_letters.append(encryption_key[index])
        else:
            encrypted_word_letters.append(l)

    return "".join(encrypted_word_letters)


def keyword_cipher(msg, keyword):
    encryption_key = generate_encryption_key(keyword)

    return encrypt_msg(msg, encryption_key)


# print(keyword_cipher("Welcome home", "secret"))
# print(keyword_cipher("hello", "wednesday"))
# print(keyword_cipher("HELLO", "wednesday"))
# print(keyword_cipher("HeLlO", "wednesday"))
# print(keyword_cipher("WELCOME HOME", "gridlocked"))
# print(keyword_cipher("alpha bravo charlie", "delta"))
# print(keyword_cipher("Home Base", "seven"))
# print(keyword_cipher("basecamp", "covert"))
# print(keyword_cipher("one two three", "rails"))
# print(keyword_cipher("Test", "unbuntu"))
