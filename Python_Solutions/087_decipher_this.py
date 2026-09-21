def decipher_this(s):
    words = s.split()
    decrypted_words = []

    for word in words:
        i = 0
        while i < len(word):
            symbol = word[i]
            if symbol.isdigit():
                i += 1
            else:
                break

        decrypted_word = chr(int(word[:i]))

        if len(word) - i == 1:
            decrypted_word += word[-1]
        elif len(word) - i > 1:
            decrypted_word = f"{decrypted_word}{word[-1]}{word[i+1:-1]}{word[i]}"

        decrypted_words.append(decrypted_word)

    return " ".join(decrypted_words)


# print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
# print(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"))
# print(decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"))
# print(decipher_this("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"))
# print(decipher_this("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"))
