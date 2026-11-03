def count_adjacent_pairs(st):
    words = [word.lower() for word in st.split()]
    pairs_counter = 0
    current_word = ""
    current_word_counter = 1

    for word in words:
        if word == current_word:
            current_word_counter += 1
            if current_word_counter == 2:
                pairs_counter += 1
        else:
            current_word_counter = 1
            current_word = word

    return pairs_counter


# print(count_adjacent_pairs(""))
# print(count_adjacent_pairs("orange Orange kiwi pineapple apple"))
# print(count_adjacent_pairs("banana banana banana"))
# print(count_adjacent_pairs("banana banana banana terracotta banana terracotta terracotta pie!"))
# print(count_adjacent_pairs("pineapple apple"))
