def sakura_fall(v):
    return 400 / v if v > 0 else 0


assert sakura_fall(5) == 80
assert sakura_fall(10) == 40
assert sakura_fall(-1) == 0
