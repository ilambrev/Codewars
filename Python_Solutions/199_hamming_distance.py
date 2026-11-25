def hamming(a, b):
    return len([1 for i in range(len(a)) if a[i] != b[i]])


# print(hamming("hello world", "hello tokyo"))
# print(hamming("a man a plan a canal", "a man a plan sobanal"))
# print(hamming("hamming and cheese", "Hamming and Cheese"))
# print(hamming("espresso", "Expresso"))
# print(hamming("old father, old artificer", "of my soul the uncreated "))
