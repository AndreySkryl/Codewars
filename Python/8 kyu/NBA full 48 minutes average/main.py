def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    return float('{:.1f}'.format(ppg * (48 / mpg)))


assert nba_extrap(12, 20) == 28.8
assert nba_extrap(10, 10) == 48.0
assert nba_extrap(5, 17) == 14.1
assert nba_extrap(0, 0) == 0
assert nba_extrap(30.8, 34.7) == 42.6
assert nba_extrap(22.9, 33.8) == 32.5
