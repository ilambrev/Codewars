def scramble(strng, array):
    new_order = list(strng)

    for i in range(len(new_order)):
        new_order[array[i]] = strng[i]

    return ''.join(new_order)

# print(scramble('abcd', [0, 3, 1, 2]))
# print(scramble('sc301s', [4,0,3,1,5,2]))
# print(scramble('bskl5', [2,1,4,3,0]))