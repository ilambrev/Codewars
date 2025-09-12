def get_consective_items(items, key):
    longest_sequence = 0
    counter = 0
    items_str = str(items)
    key_str = str(key)

    for item in items_str:
        if item == key_str:
            counter += 1
        else:
            if counter > longest_sequence:
                longest_sequence = counter

            counter = 0

    return longest_sequence if longest_sequence >= counter else counter

# print(get_consective_items('abcdaaadse', 'a'))
# print(get_consective_items('abcdaaadse', 'z'))
# print(get_consective_items(90000, 0))
# print(get_consective_items('ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii', 'i'))