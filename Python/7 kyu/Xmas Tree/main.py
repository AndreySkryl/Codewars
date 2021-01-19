def xMasTree(n):
    count_of_sharps = [2*i + 1 for i in range(n)] + [1, 1]
    width = 2*n - 1
    tree = [
        '{:{fill}{align}{width}}'.format('#' * count_of_sharp, fill='_', align='^', width=width)
        for count_of_sharp in count_of_sharps
    ]
    return tree


assert xMasTree(3) == ['__#__', '_###_', '#####', '__#__', '__#__']
assert xMasTree(7) == ['______#______', '_____###_____', '____#####____', '___#######___', '__#########__',
                       '_###########_', '#############', '______#______', '______#______']
assert xMasTree(2) == ['_#_', '###', '_#_', '_#_']
assert xMasTree(4) == ['___#___', '__###__', '_#####_', '#######', '___#___', '___#___']
assert xMasTree(6) == ['_____#_____', '____###____', '___#####___', '__#######__', '_#########_', '###########',
                       '_____#_____', '_____#_____']
