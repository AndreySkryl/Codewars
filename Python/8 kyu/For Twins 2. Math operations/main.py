def ice_brick_volume(radius, bottle_length, rim_length):
    width = 2**0.5 * radius
    height = bottle_length - rim_length
    return int(width * width * height)


assert ice_brick_volume(1, 10, 2) == 16
assert ice_brick_volume(5, 30, 7) == 1150
