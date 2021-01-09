def maps(array):
    return list(map(lambda x: x * 2, array))


assert maps([1, 2, 3]) == [2, 4, 6]
assert maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
assert maps([]) == []
