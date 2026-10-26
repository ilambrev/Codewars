def linked_sort(a_to_sort, a_linked, key=lambda x: str(x[0])):
    temp_list = sorted([[a_to_sort[i], a_linked[i]] for i in range(len(a_to_sort))], key=key)

    for i in range(len(temp_list)):
        s, l = temp_list[i]
        a_to_sort[i] = s
        a_linked[i] = l

    return a_to_sort


# print(linked_sort([1, 6, 5, 0], ['house', 'car', 'pen', 'jeans']))
# print(linked_sort([-71, -6, 35, 0], [0, "Hello", 32, True]))
