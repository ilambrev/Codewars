def count_elements(elements, lst, position):
    for element in lst:
        counter = elements.setdefault(element, [0, 0, 0])
        counter[position] += 1


def common(a, b, c):
    elements = {}
    count_elements(elements, a, 0)
    count_elements(elements, b, 1)
    count_elements(elements, c, 2)

    return sum(e * min(elements[e]) for e in elements)


# print(common([1, 2, 3], [5, 3, 2], [7, 3, 2]))
# print(common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]))
# print(common([1], [1], [1]))
# print(common([1], [1], [2]))
