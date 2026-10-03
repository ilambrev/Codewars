def calculate_final_coordinates(path, moves):
    row = 0
    col = 0

    for move in path:
        step = moves[move]
        row += step[0]
        col += step[1]

    return [row, col]


def path_finding(path):
    launderette_location_1 = "eneen"
    launderette_location_2 = "wnwnwwn"
    moves = {
        "n": [-1, 0],
        "e": [0, 1],
        "s": [1, 0],
        "w": [0, -1]
    }

    location_1_final_coordinates = calculate_final_coordinates(launderette_location_1, moves)
    location_2_final_coordinates = calculate_final_coordinates(launderette_location_2, moves)
    robot_final_coordinates = calculate_final_coordinates(path, moves)

    return robot_final_coordinates == location_1_final_coordinates or robot_final_coordinates == location_2_final_coordinates


# print(path_finding("eneen"))
# print(path_finding("wnwnwwn"))
# print(path_finding("seennen"))
# print(path_finding("nsnnenwwswwwn"))
# print(path_finding("nsnnnenwnwswwwn"))
# print(path_finding("nsnsnsnsnsnsnseww"))
# print(path_finding("neswneswwsne"))
