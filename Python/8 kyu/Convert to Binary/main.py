def to_binary(n):
    return int(bin(n)[2:])


assert to_binary(1) == 1
assert to_binary(2) == 10
assert to_binary(3) == 11
assert to_binary(5) == 101
