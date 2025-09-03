def sep_str(st):
    words = st.split()
    max_word_length = max(map(len, words)) if words else 0
    result = []

    for row in range(max_word_length):
        result_row = []
        for col in range(len(words)):
            if row < len(words[col]):
                result_row.append(words[col][row])
            else:
                result_row.append("")

        result.append(result_row)

    return result

# print(sep_str("Just Live Life Man"))
# print(sep_str("The Mitochondria is the powerhouse of the cell"))
# print(sep_str(""))