def find_even_index(arr):
    divided_index = 0
    summa_left, summa_right = sum(arr[:divided_index]), sum(arr[divided_index + 1:])
    while divided_index < len(arr) - 1 and summa_left != summa_right:
        divided_index += 1
        summa_left += arr[divided_index - 1]
        summa_right -= arr[divided_index]
    return divided_index if summa_left == summa_right else -1


assert find_even_index([1, 2, 3, 4, 3, 2, 1]) == 3
assert find_even_index([1, 100, 50, -51, 1, 1]) == 1
assert find_even_index([1, 2, 3, 4, 5, 6]) == -1
assert find_even_index([20, 10, 30, 10, 10, 15, 35]) == 3
assert find_even_index([20, 10, -80, 10, 10, 15, 35]) == 0
assert find_even_index([10, -80, 10, 10, 15, 35, 20]) == 6
assert find_even_index(list(range(1, 100))) == -1
assert find_even_index([0, 0, 0, 0, 0]) == 0
assert find_even_index([-1, -2, -3, -4, -3, -2, -1]) == 3
assert find_even_index(list(range(-100, -1))) == -1
