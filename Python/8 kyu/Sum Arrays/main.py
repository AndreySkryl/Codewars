def sum_array(a):
    return sum(a)


assert sum_array([]) == 0
assert sum_array([1, 2, 3]) == 6
assert sum_array([1.1, 2.2, 3.3]) == 6.6
assert sum_array([4, 5, 6]) == 15
assert sum_array(range(101)) == 5050
