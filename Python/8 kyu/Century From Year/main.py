def century(year):
    return year // 100 + (1 if year % 100 else 0)


assert century(1705) == 18
assert century(1900) == 19
assert century(1601) == 17
assert century(2000) == 20
assert century(356) == 4
assert century(89) == 1
