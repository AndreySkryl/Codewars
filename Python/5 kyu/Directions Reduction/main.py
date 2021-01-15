def dirReduc(array):
    direction_reduce = []

    for item in array:
        if direction_reduce and direction_reduce[-1]:
            last_element = direction_reduce[-1]
            if (last_element == 'NORTH' and item == 'SOUTH') or \
                    (last_element == 'SOUTH' and item == 'NORTH') or \
                    (last_element == 'WEST' and item == 'EAST') or \
                    (last_element == 'EAST' and item == 'WEST'):
                direction_reduce.pop()
            else:
                direction_reduce.append(item)
        else:
            direction_reduce.append(item)

    return direction_reduce


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
assert dirReduc(a) == ['WEST']
u = ["NORTH", "WEST", "SOUTH", "EAST"]
assert dirReduc(u) == ["NORTH", "WEST", "SOUTH", "EAST"]
