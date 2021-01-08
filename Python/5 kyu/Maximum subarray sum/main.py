def max_sequence(arr):
    return max([sum(arr[i:j]) for i in range(len(arr) + 1) for j in range(len(arr) + 1)])
    # if len(arr) == 0:
    #     return 0
    #
    # max_sum = 0
    # for i in range(len(arr)):
    #     for j in range(i, len(arr)):
    #         summa = sum(arr[i:j+1])
    #         max_sum = max(max_sum, summa)
    # return max_sum


assert max_sequence([]) == 0
assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_sequence([-1, 0]) == 0
