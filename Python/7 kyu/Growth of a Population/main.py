def nb_year(p0, percent, aug, p):
    percent *= 0.01
    counter = 1
    while True:
        p0 += p0 * percent + aug
        if p0 < p:
            counter += 1
        else:
            break
    return counter


assert nb_year(1500, 5, 100, 5000) == 15
assert nb_year(1500000, 2.5, 10000, 2000000) == 10
assert nb_year(1500000, 0.25, 1000, 2000000) == 94
