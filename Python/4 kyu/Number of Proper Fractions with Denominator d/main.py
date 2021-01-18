def proper_fractions(n):
    phi = n > 1 and n
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    if n > 1:
        phi -= phi // n
    return phi


assert proper_fractions(1) == 0
assert proper_fractions(2) == 1
assert proper_fractions(5) == 4
assert proper_fractions(15) == 8
assert proper_fractions(25) == 20
