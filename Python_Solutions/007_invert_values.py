def invert(lst):
    inverted_list = []
    for num in lst:
        inverted_list.append(num * -1)

    return inverted_list

# print(invert([1, 2, 3, 4, 5]))
# print(invert([1, -2, 3, -4, 5]))
# print(invert([]))