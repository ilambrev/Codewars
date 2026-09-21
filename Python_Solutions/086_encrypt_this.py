def encrypt_this(text):
    words = text.split()
    if words:
        encrypted_words = []
        encrypted_word = ""
        for word in words:
            if len(word) == 1:
                encrypted_word = str(ord(word))
            elif len(word) == 2:
                encrypted_word = str(ord(word[0])) + word[1]
            elif len(word) > 2:
                encrypted_word = str(ord(word[0])) + word[-1] + word[2:-1] + word[1]

            encrypted_words.append(encrypted_word)

        return " ".join(encrypted_words)
    else:
        return text


# print(encrypt_this(""))
# print(encrypt_this("A wise old owl lived in an oak"))
# print(encrypt_this("The more he saw the less he spoke"))
# print(encrypt_this("The less he spoke the more he heard"))
# print(encrypt_this("Why can we not all be like that wise old bird"))
# print(encrypt_this("Thank you Piotr for all your help"))
