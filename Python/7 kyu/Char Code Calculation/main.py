def calc(x):
    total_1 = ''.join([str(ord(i)) for i in x])
    total_2 = total_1.replace('7', '1')
    return sum(int(i) for i in total_1) - sum(int(i) for i in total_2)


assert calc('ABC') == 6
assert calc('abcdef') == 6
assert calc('ifkhchlhfd') == 6
assert calc('aaaaaddddr') == 30
assert calc('jfmgklf8hglbe') == 6
assert calc('jaam') == 12
assert calc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') == 96
