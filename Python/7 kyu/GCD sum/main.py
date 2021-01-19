from math import gcd


def solve(s, g):
    for i in range(1, s):
        if gcd(s, i) == g and gcd(s, s - i) == g:
            return min(i, s-i), max(i, s-i)
    return -1


assert solve(6, 3) == (3, 3)
assert solve(8, 2) == (2, 6)
assert solve(10, 3) == -1
assert solve(12, 4) == (4, 8)
assert solve(12, 5) == -1
