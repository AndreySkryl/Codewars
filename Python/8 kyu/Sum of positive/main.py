def positive_sum(array):
    return sum(filter(lambda x: x > 0, array))


assert positive_sum([1, 2, 3, 4, 5]) == 15
assert positive_sum([1, -2, 3, 4, 5]) == 13
assert positive_sum([-1, 2, 3, 4, -5]) == 9
assert positive_sum([]) == 0
assert positive_sum([-1, -2, -3, -4, -5]) == 0
