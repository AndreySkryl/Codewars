def enough(cap, on, wait):
    return 0 if wait + on < cap else wait + on - cap


assert enough(10, 5, 5) == 0
assert enough(100, 60, 50) == 10
assert enough(20, 5, 5) == 0
