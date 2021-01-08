# TODO: пересмотреть

def last_digit(number, degree):
    return pow(number, degree, 10)
    # if degree == 0:
    #     return 1
    #
    # degree_mod = degree % 4
    # number_mod = number % 10
    # if degree_mod == 0:
    #     if number_mod == 5:
    #         return number_mod
    #     elif number_mod & 1:
    #         return 1
    #     elif number_mod == 0:
    #         return number_mod
    #     else:
    #         return 6
    # elif degree_mod == 1:
    #     return number_mod
    # elif degree_mod == 2:
    #     return int(str(number_mod ** 2)[-1])
    # elif degree_mod == 3:
    #     return int(str(number_mod ** 3)[-1])


assert last_digit(6, 0) == 1
assert last_digit(4, 1) == 4
assert last_digit(4, 2) == 6
assert last_digit(9, 7) == 9
assert last_digit(10, 10 ** 10) == 0
assert last_digit(2 ** 200, 2 ** 300) == 6
assert last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651) == 7
