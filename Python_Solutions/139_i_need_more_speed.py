def reverse(seq):
    for i in range(len(seq) // 2):
        seq[i], seq[len(seq) - i - 1] = seq[len(seq) - i - 1], seq[i]

    return seq


# print(reverse([1, 2, 3, 4, 5]))
# print(reverse(['?', 'you', 'are', 'how', 'world', 'hello']))
# print(reverse([{'b': 2}, {'a': 1}]))
