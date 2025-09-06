def available_moves(position):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    digits = ['1', '2', '3', '4', '5', '6', '7', '8']
    possible_positions = []

    def move_right(letter, digit):
        for i in range(letters.index(letter) + 1, len(letters)):
            possible_positions.append(f'{letters[i]}{digit}')

    def move_down(letter, digit):
        for i in range(digits.index(digit) + 1, len(digits)):
            possible_positions.append(f'{letter}{digits[i]}')

    def move_left(letter, digit):
        for i in range(0, letters.index(letter)):
            possible_positions.append(f'{letters[i]}{digit}')

    def move_up(letter, digit):
        for i in range(0, digits.index(digit)):
            possible_positions.append(f'{letter}{digits[i]}')

    def move_right_up(letter, digit):
        row_index = digits.index(digit) - 1
        col_index = letters.index(letter) + 1

        while row_index >= 0 and col_index < len(letters):
            possible_positions.append(
                f'{letters[col_index]}{digits[row_index]}')
            row_index -= 1
            col_index += 1

    def move_right_down(letter, digit):
        row_index = digits.index(digit) + 1
        col_index = letters.index(letter) + 1

        while row_index < len(digits) and col_index < len(letters):
            possible_positions.append(
                f'{letters[col_index]}{digits[row_index]}')
            row_index += 1
            col_index += 1

    def move_left_up(letter, digit):
        row_index = digits.index(digit) - 1
        col_index = letters.index(letter) - 1

        while row_index >= 0 and col_index >= 0:
            possible_positions.append(
                f'{letters[col_index]}{digits[row_index]}')
            row_index -= 1
            col_index -= 1

    def move_left_down(letter, digit):
        row_index = digits.index(digit) + 1
        col_index = letters.index(letter) - 1

        while row_index < len(digits) and col_index >= 0:
            possible_positions.append(
                f'{letters[col_index]}{digits[row_index]}')
            row_index += 1
            col_index -= 1

    if (position
            and isinstance(position, str)
            and len(position) == 2
            and position[0] in letters
            and position[1] in digits):
        move_right(position[0], position[1])
        move_down(position[0], position[1])
        move_left(position[0], position[1])
        move_up(position[0], position[1])
        move_right_up(position[0], position[1])
        move_right_down(position[0], position[1])
        move_left_up(position[0], position[1])
        move_left_down(position[0], position[1])

    possible_positions.sort()

    return possible_positions

# print(available_moves('A1'))
# print(available_moves('C5'))
# print(available_moves('H3'))
# print(available_moves(None))
# print(available_moves([1, 2, 3]))
# print(available_moves('work?'))
# print(available_moves('A10'))
# print(available_moves('B0'))
# print(available_moves(2))