def get_sum(a, b):
    return sum([x for x in range(min(a, b), max(a, b) + 1)])


assert get_sum(0, 1) == 1
assert get_sum(0, -1) == -1

assert get_sum(1, 0) == 1
assert get_sum(1, 2) == 3
assert get_sum(0, 1) == 1
assert get_sum(1, 1) == 1
assert get_sum(-1, 0) == -1
assert get_sum(-1, 2) == 2