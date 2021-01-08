def summation(number):
    return sum(i for i in range(number + 1))


assert summation(1) == 1
assert summation(8) == 36
assert summation(22) == 253
assert summation(100) == 5050
assert summation(213) == 22791
