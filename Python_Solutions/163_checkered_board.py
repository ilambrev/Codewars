def checkered_board(n):
    white = "■"
    black = "□"

    elements = n ** 2

    if elements % 2 == 0:
        board = [black if element % 2 == 0 else white for element in range(elements)]
    else:
        board = [white if element % 2 == 0 else black for element in range(elements)]

    board = [" ".join(board[i:i+n]) for i in range(0, len(board), n)]
    board = [board[i] if i % 2 == 0 else board[i][::-1] for i in range(len(board))]

    return "\n".join(board)


# print(checkered_board(2))
# print(checkered_board(10))
# print(checkered_board(3))
# print(checkered_board(7))
