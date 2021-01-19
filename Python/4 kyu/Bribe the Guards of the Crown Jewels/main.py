def least_bribes(bribes):
    
    return 0


assert least_bribes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 26
assert least_bribes([1, 2, 3, 4, 5]) == 9
assert least_bribes([5, 1, 2, 4, 3]) == 8
assert least_bribes([3, 2, 5, 4, 1]) == 10
assert least_bribes([r * 53 + q for m in range(1, 51) for q, r in (divmod(m, 7),)]) == 663
assert least_bribes([r * 53 + q for m in range(1, 101) for q, r in (divmod(m, 7),)]) == 702
