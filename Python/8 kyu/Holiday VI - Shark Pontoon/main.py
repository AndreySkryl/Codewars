def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    return 'Alive!' if pontoon_distance / you_speed < shark_distance / shark_speed else 'Shark Bait!'


assert shark(12, 50, 4, 8, True) == "Alive!"
assert shark(7, 55, 4, 16, True) == "Alive!"
assert shark(24, 0, 4, 8, True) == "Shark Bait!"
