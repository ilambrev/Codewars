def get_start_coordinates(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "x":
                return [i, j]

    return []


def get_password(grid, directions):
    coordinates = get_start_coordinates(grid)
    password = ""

    for direction in directions:
        if direction in ["right", "rightT"]:
            coordinates[1] += 1
        elif direction in ["left", "leftT"]:
            coordinates[1] -= 1
        elif direction in ["up", "upT"]:
            coordinates[0] -= 1
        elif direction in ["down", "downT"]:
            coordinates[0] += 1

        if "T" in direction:
            password += grid[coordinates[0]][coordinates[1]]

    return password


# grid = [
#     ["x", "l", "m"],
#     ["o", "f", "c"],
#     ["k", "i", "t"]
# ]

# directions = ["rightT", "down", "leftT", "right", "rightT", "down", "left", "leftT"]

# print(get_password(grid, directions))
