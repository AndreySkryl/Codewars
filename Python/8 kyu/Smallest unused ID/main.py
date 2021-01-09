def next_id(array):
    if not array:
        return 0

    set_array = sorted(set(array))
    return [v for v in range(max(array) + 2) if v not in set_array][0]


assert next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
assert next_id([5, 4, 3, 2, 1]) == 0
assert next_id([0, 1, 2, 3, 5]) == 4
assert next_id([0, 0, 0, 0, 0, 0]) == 1
assert next_id([]) == 0
