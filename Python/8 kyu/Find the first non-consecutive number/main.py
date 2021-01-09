def first_non_consecutive(array):
    if len(array) <= 2:
        return None

    for i in range(1, len(array)):
        if array[i] - array[i - 1] != 1:
            return array[i]


assert first_non_consecutive([1, 2, 3, 4, 6, 7, 8]) == 6
assert first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]) is None
assert first_non_consecutive([4, 6, 7, 8, 9, 11]) == 6
assert first_non_consecutive([4, 5, 6, 7, 8, 9, 11]) == 11
assert first_non_consecutive([31, 32]) is None
assert first_non_consecutive([-3, -2, 0, 1]) == 0
assert first_non_consecutive([-5, -4, -3, -1]) == -1
