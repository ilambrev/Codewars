def decrypt(test_key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    return "".join(str(test_key.count(letter)) for letter in alphabet)


# print(decrypt("$aaaa#bbb*ccfff!z"))
# print(decrypt("z$aaa#ccc%eee1234567890"))
