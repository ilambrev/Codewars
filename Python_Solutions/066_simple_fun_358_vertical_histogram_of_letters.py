def vertical_histogram_of(s: str) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = {}

    for symbol in s:
        if symbol in alphabet:
            letters[symbol] = letters.get(symbol, 0) + 1

    max_count = max(letters.values()) if letters else 0

    rows = []

    letters = {k: v for k, v in sorted(
        letters.items(), key=lambda item: item[0])}

    for i in range(max_count, 0, -1):
        row = []
        for letter, repeats_number in letters.items():
            if repeats_number >= i:
                row.append("*")
            else:
                row.append(" ")
        rows.append(" ".join(row).rstrip())

    rows.append(" ".join(letters.keys()))

    return "\n".join(rows)


# print(vertical_histogram_of("XXY YY ZZZ123ZZZ AAA BB C"))
# print(vertical_histogram_of("AAABBC"))
# print(vertical_histogram_of("A"))
# print(vertical_histogram_of(""))
# print(vertical_histogram_of("abc123"))
