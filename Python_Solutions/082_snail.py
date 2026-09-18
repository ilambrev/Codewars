def snail(snail_map):
    n = len(snail_map)
    snail_list = []

    if n == 0 or len(snail_map[0]) == 0:
        return snail_list

    snail_map_passed = [[0] * n for _ in range(n)]

    row = 0
    col = 0

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction_index = 0
    direction = directions[direction_index]

    for i in range(n * n):
        if snail_map_passed[row][col] == 0:
            snail_list.append(snail_map[row][col])
            snail_map_passed[row][col] = 1

        next_row = row + direction[0]
        next_col = col + direction[1]

        if next_row < 0 or next_row == n or next_col < 0 or next_col == n or snail_map_passed[next_row][next_col] == 1:
            direction_index = (direction_index + 1) % len(directions)
            direction = directions[direction_index]

        row = row + direction[0]
        col = col + direction[1]

    return snail_list


# array = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# print(snail(array))

# array = [[1, 2, 3],
#          [8, 9, 4],
#          [7, 6, 5]]
# print(snail(array))

# array = [[]]
# print(snail(array))
