def sum_str(a, b):
    return str(sum(int(x) for x in [a, b] if x.isnumeric()))


assert sum_str("4", "5") == "9"
assert sum_str("34", "5") == "39"

assert sum_str("9", "") == "9", "x + empty = x"
assert sum_str("", "9") == "9", "empty + x = x"
assert sum_str("", "") == "0"
