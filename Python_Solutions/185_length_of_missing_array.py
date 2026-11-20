def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays or None in array_of_arrays or [] in array_of_arrays:
        return 0
    
    lengths = [len(arr) for arr in sorted(array_of_arrays, key=lambda arr: len(arr))]

    for i in range(1, len(lengths)):
        if lengths[i] - lengths[i-1] > 1:
            return lengths[i] - 1

    return 0


# print(get_length_of_missing_array([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]))
# print(get_length_of_missing_array([[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]))
# print(get_length_of_missing_array([[None], [None, None, None]]))
# print(get_length_of_missing_array([["a", "a", "a"], ["a", "a"], ["a", "a", "a", "a"], ["a"], ["a", "a", "a", "a", "a", "a"]]))
