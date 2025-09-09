values = {
    'queen': 9,
    'rook': 5,
    'bishop': 3,
    'knight': 3,
    'pawn': 1,
}

def pieces_value(arr, s):
    value = 0
    for row in arr:
        for field in row:
            if field == ' ':
                continue
            color, piece = field.split('-')
            if color == s[0] and piece in values:
                value += values.get(piece)

    return value

# board1 = [['b-bishop', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#           [' ', ' ', 'b-queen', ' ', ' ', ' ', ' ', 'w-queen'],
#           [' ', 'b-king', ' ', 'b-pawn', 'w-rook', ' ', ' ', ' '],
#           [' ', ' ', ' ', ' ', 'w-pawn', ' ', ' ', ' '],
#           [' ', ' ', ' ', ' ', ' ', 'w-bishop', ' ', ' '],
#           ['w-king', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#           [' ', ' ', 'b-pawn', 'b-pawn', ' ', ' ', ' ', ' '],
#           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
#
# board2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#           [' ', ' ', ' ', ' ', ' ', 'b-king', ' ', ' '],
#           [' ', 'b-knight', ' ', ' ', 'w-pawn', ' ', ' ', ' '],
#           [' ', ' ', 'w-bishop', ' ', ' ', ' ', ' ', ' '],
#           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#           [' ', 'w-pawn', ' ', ' ', ' ', 'w-pawn', ' ', ' '],
#           [' ', ' ', ' ', ' ', 'b-pawn', ' ', ' ', ' '],
#           [' ', 'w-rook', ' ', ' ', ' ', 'w-king', ' ', ' ']]
#
# board3 = [[' ', ' ', ' ', ' ', 'b-king', ' ', ' ', ' '],
#           [' ', 'b-bishop', ' ', ' ', 'b-pawn', 'b-pawn', ' ', ' '],
#           [' ', ' ', ' ', ' ', 'b-knight', ' ', ' ', ' '],
#           [' ', ' ', 'w-queen', ' ', ' ', ' ', ' ', ' '],
#           [' ', 'w-bishop', ' ', ' ', ' ', ' ', ' ', ' '],
#           [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'b-rook'],
#           [' ', 'w-pawn', 'w-pawn', ' ', ' ', ' ', ' ', ' '],
#           [' ', ' ', 'w-king', ' ', ' ', ' ', ' ', ' ']]
#
# print(pieces_value(board1, 'white'))
# print(pieces_value(board1, 'black'))
# print(pieces_value(board2, 'white'))
# print(pieces_value(board2, 'black'))
# print(pieces_value(board3, 'white'))
# print(pieces_value(board3, 'black'))