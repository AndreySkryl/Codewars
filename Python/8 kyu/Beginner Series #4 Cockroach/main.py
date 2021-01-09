def cockroach_speed(s):
    return int(s * 100000 / 3600)


assert cockroach_speed(1.08) == 30
assert cockroach_speed(1.09) == 30
assert cockroach_speed(0) == 0
