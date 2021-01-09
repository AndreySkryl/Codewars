def is_divide_by(number, a, b):
    return all([number % i == 0 for i in [a, b]])


assert is_divide_by(-12, 2, -6) == True
assert is_divide_by(-12, 2, -5) == False
assert is_divide_by(45, 1, 6) == False
assert is_divide_by(45, 5, 15) == True
assert is_divide_by(4, 1, 4) == True
assert is_divide_by(15, -5, 3) == True
