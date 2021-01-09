def invert(lst):
    return [-x for x in lst]


assert invert([1, 2, 3, 4, 5]) == [-1, -2, -3, -4, -5]
assert invert([1, -2, 3, -4, 5]) == [-1, 2, -3, 4, -5]
assert invert([]) == []
