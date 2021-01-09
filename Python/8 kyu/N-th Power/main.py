def index(array, n):
    return array[n] ** n if 0 <= n < len(array) else -1


assert index([1, 2, 3, 4], 2) == 9
assert index([1, 3, 10, 100], 3) == 1000000
