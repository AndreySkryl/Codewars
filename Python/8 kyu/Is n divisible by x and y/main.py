def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


assert is_divisible(3,2,2) == False
assert is_divisible(3,3,4) == False
assert is_divisible(12,3,4) == True
assert is_divisible(8,3,4) == False
