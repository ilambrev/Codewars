def custom_christmas_tree(chars, n):
    tree_parts = []
    char_index = 0

    for i in range(n):
        spaces = n - 1 - i
        leaves = []

        for j in range(i + 1):
            leaves.append(chars[char_index])
            char_index = (char_index + 1) % len(chars)

        row = " " * spaces + " ".join(leaves)
        tree_parts.append(row)

    trunk_parts = [f"{' ' * (n - 1)}|" for _ in range(int(n / 3))]
    tree_parts += trunk_parts

    return "\n".join(tree_parts)


# print(custom_christmas_tree("*@o",3))
# print(custom_christmas_tree("*@o",6))
# print(custom_christmas_tree("1234",6))
# print(custom_christmas_tree("123456789",3))
