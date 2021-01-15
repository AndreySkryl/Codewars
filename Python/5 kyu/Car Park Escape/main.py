def escape(carpark):
    level = position = -1
    for i, row in enumerate(carpark):
        for j, column in enumerate(row):
            if column == 2:
                level = i
                position = j
                break

    result = []
    while not (level == len(carpark) - 1 and position == len(carpark[0]) - 1):
        if level == len(carpark) - 1:
            break
        else:
            index_of_1 = carpark[level].index(1)
            if index_of_1 < position:
                result.append(f'L{position - index_of_1}')
            elif index_of_1 > position:
                result.append(f'R{index_of_1 - position}')
            result.append('D1')
            position = index_of_1
            level += 1

    cleared_result = []
    down_counter = 0
    for item in result:
        if item == 'D1':
            down_counter += 1
        else:
            if down_counter != 0:
                cleared_result.append(f'D{down_counter}')
                down_counter = 0
            cleared_result.append(item)
    if down_counter != 0:
        cleared_result.append(f'D{down_counter}')
        down_counter = 0

    if position != len(carpark[0]) - 1:
        cleared_result.append(f'R{(len(carpark[0]) - 1) - position}')
        position = len(carpark[0]) - 1

    return cleared_result


carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]
result = ["L4", "D1", "R4"]
assert escape(carpark) == result

carpark = [[2, 0, 0, 1, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0]]
result = ["R3", "D2", "R1"]
assert escape(carpark) == result

carpark = [[0, 2, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]
result = ["R3", "D3"]
assert escape(carpark) == result

carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]
result = ["L4", "D1", "R4", "D1", "L4", "D1", "R4"]
assert escape(carpark) == result

carpark = [[0, 0, 0, 0, 2]]
result = []
assert escape(carpark) == result
