from math import sqrt


def cipher_text(plain_text):
    filtered_text = "".join([s for s in plain_text.lower() if s.isalpha()])
    length = len(filtered_text)
    a = round(sqrt(length))
    b = a if a ** 2 >= length else a + 1
    total_symbol_count = a * b

    if total_symbol_count > length:
        filtered_text += " " * (total_symbol_count - length)

    text_rows = [filtered_text[i*b:i*b+b] for i in range(a)]

    return " ".join(["".join(row[i] for row in text_rows) for i in range(b)])


# print(cipher_text("When nobody is around, the trees gossip about the people who have walked under them."))
# print(cipher_text("I want a giraffe, but I\"m a turtle eating waffles."))
# print(cipher_text("Dolores wouldn\"t have eaten the meal if she had known what it actually was."))
# print(cipher_text("She says she has the ability to hear the soundtrack of your life."))
# print(cipher_text("I\"ve always wanted to go to Tajikistan, but my cat would miss me."))
# print(cipher_text("###"))
