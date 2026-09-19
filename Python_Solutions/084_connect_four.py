def create_board(cols, rows):
    return [["E"] * cols for _ in range(rows)]


def check_for_winner(board, first_player, second_player):
    result = check_rows_for_winner(board, first_player, second_player)

    if not result == -1:
        return result

    result = check_cols_for_winner(board, first_player, second_player)

    if not result == -1:
        return result

    result = check_right_diags_for_winner(board, first_player, second_player)

    if not result == -1:
        return result

    result = check_left_diags_for_winner(board, first_player, second_player)

    if not result == -1:
        return result

    return "D"


def check_rows_for_winner(board, first_player, second_player):
    pattern_first_player = first_player * 4
    pattern_second_player = second_player * 4

    for row in board:
        if pattern_first_player in "".join(row):
            return first_player

        if pattern_second_player in "".join(row):
            return second_player

    return -1


def check_cols_for_winner(board, first_player, second_player):
    rows = len(board)
    cols = len(board[0])

    pattern_first_player = first_player * 4
    pattern_second_player = second_player * 4

    for i in range(cols):
        col = []
        for j in range(rows):
            col.append(board[j][i])

        if pattern_first_player in "".join(col):
            return first_player

        if pattern_second_player in "".join(col):
            return second_player

    return -1


def check_right_diags_for_winner(board, first_player, second_player):
    rows = len(board)
    cols = len(board[0])

    pattern_first_player = first_player * 4
    pattern_second_player = second_player * 4

    for i in range(rows):
        diag = []
        for j in range(i, -1, -1):
            diag.append(board[i - j][j])

        if pattern_first_player in "".join(diag):
            return first_player

        if pattern_second_player in "".join(diag):
            return second_player

    for i in range(rows):
        diag = []
        for j in range(rows - i):
            diag.append(board[j + i][cols - 1 - j])

        if pattern_first_player in "".join(diag):
            return first_player

        if pattern_second_player in "".join(diag):
            return second_player

    return -1


def check_left_diags_for_winner(board, first_player, second_player):
    rows = len(board)
    cols = len(board[0])

    pattern_first_player = first_player * 4
    pattern_second_player = second_player * 4

    for i in range(rows - 1, -1, -1):
        diag = []
        for j in range(rows - i):
            diag.append(board[i + j][j])

        if pattern_first_player in "".join(diag):
            return first_player

        if pattern_second_player in "".join(diag):
            return second_player

    for i in range(rows):
        diag = []
        for j in range(i, -1, -1):
            diag.append(board[i - j][cols - 1 - j])

        if pattern_first_player in "".join(diag):
            return first_player

        if pattern_second_player in "".join(diag):
            return second_player

    return -1


def who_is_winner(pieces_position_list):
    rows = 6
    cols = 7
    results = {
        "Y": "Yellow",
        "R": "Red",
        "D": "Draw"
    }
    board = create_board(cols, rows)
    cols_indexes = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6
    }
    rows_values = [5] * 7
    first_player = ""
    second_player = ""

    for p in pieces_position_list:
        col, player = p.split("_")
        player_first_letter = player[0]

        if not first_player and not second_player:
            first_player = player_first_letter
            second_player = "R" if first_player == "Y" else "Y"

        current_col_index = cols_indexes[col]
        board[rows_values[current_col_index]
              ][current_col_index] = player_first_letter
        rows_values[current_col_index] -= 1

        result = check_for_winner(board, first_player, second_player)

        if not result == "D":
            return results[result]

    return results["D"]


# print(who_is_winner([
# "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
# "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
# "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
# ]))

# print(who_is_winner([
# "C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
# "G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
# "D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
# "C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
# "E_Yellow", "E_Red"
# ]))

# print(who_is_winner([
# "F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
# "B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
# "F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
# "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
# "B_Yellow", "B_Red"
# ]))

# print(who_is_winner([
# "A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
# "G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
# ]))

# print(who_is_winner([
# "A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
# ]))

# print(who_is_winner([
# "A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
# ]))
