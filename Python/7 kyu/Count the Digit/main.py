def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))


assert nb_dig(5750, 0) == 4700
assert nb_dig(11011, 2) == 9481
assert nb_dig(12224, 8) == 7733
assert nb_dig(11549, 1) == 11905
