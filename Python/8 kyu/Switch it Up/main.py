def switch_it_up(number):
    table = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    return table[number]


assert switch_it_up(0) == "Zero"
assert switch_it_up(9) == "Nine"
