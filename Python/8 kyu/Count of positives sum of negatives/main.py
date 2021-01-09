def count_positives_sum_negatives(array):
    if not array:
        return []
    count_positives = len([item for item in array if item > 0])
    sum_negatives = sum(item for item in array if item < 0)
    return [count_positives, sum_negatives]


assert count_positives_sum_negatives([1,  2,  3,  4,  5,  6,  7,  8,  9,  10,  -11,  -12,  -13,  -14,  -15]) == [10, -65]
assert count_positives_sum_negatives([0,  2,  3,  0,  5,  6,  7,  8,  9,  10,  -11,  -12,  -13,  -14]) == [8, -50]
assert count_positives_sum_negatives([1]) == [1, 0]
assert count_positives_sum_negatives([-1]) == [0, -1]
assert count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0]
assert count_positives_sum_negatives([]) == []
