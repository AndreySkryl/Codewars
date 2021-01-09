def sum_array(array):
    return 0 if array is None or not array or len(array) <= 2 \
        else sum(array) - max(array) - min(array)


assert sum_array(None) == 0
assert sum_array([]) == 0
assert sum_array([3]) == 0
assert sum_array([-3]) == 0
assert sum_array([3, 5]) == 0
assert sum_array([-3, -5]) == 0
assert sum_array([6, 2, 1, 8, 10]) == 16
assert sum_array([6, 0, 1, 10, 10]) == 17
assert sum_array([-6, -20, -1, -10, -12]) == -28
assert sum_array([-6, 20, -1, 10, -12]) == 3
