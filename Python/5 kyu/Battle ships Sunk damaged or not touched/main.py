def damaged_or_sunk(board, attacks):
    sunk = damaged = not_touched = 0

    for attack in attacks:
        row, column = -attack[1], attack[0] - 1
        board[row][column] *= -1

    from itertools import chain
    unique_values = set(chain(*board))
    unique_values.remove(0)

    for unique_value in unique_values:
        if unique_value > 0:
            if -1*unique_value in unique_values:
                damaged += 1
            else:
                not_touched += 1
        elif unique_value < 0 and abs(unique_value) not in unique_values:
            sunk += 1

    points = sunk + 0.5*damaged - not_touched
    return {'sunk': sunk, 'damaged': damaged, 'not_touched': not_touched, 'points': points}


board = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0]
]

attacks = [[3, 1], [3, 2], [3, 3]]
result = damaged_or_sunk(board, attacks)
assert result['sunk'] == 1
assert result['damaged'] == 0
assert result['not_touched'] == 0
assert result['points'] == 1

board = [
    [3, 0, 1],
    [3, 0, 1],
    [0, 2, 1],
    [0, 2, 0]
]

attacks = [[2, 1], [2, 2], [3, 2], [3, 3]]
result = damaged_or_sunk(board, attacks)
assert result['sunk'] == 1
assert result['damaged'] == 1
assert result['not_touched'] == 1
assert result['points'] == 0.5