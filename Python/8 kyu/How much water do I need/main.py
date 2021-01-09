def how_much_water(water, load, clothes):
    if clothes < load:
        return 'Not enough clothes'
    elif 2 * load < clothes:
        return 'Too much clothes'
    else:
        delta = clothes - load if clothes > load else 0
        count_of_water = water * 1.1 ** delta
        return float('{:.2f}'.format(count_of_water))


assert how_much_water(10, 10, 21) == 'Too much clothes', ''
assert how_much_water(10, 10, 2) == 'Not enough clothes', ''
assert how_much_water(10, 11, 20) == 23.58, ''
assert how_much_water(50, 15, 29) == 189.87, ''
