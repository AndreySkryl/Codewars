def namelist(names):
    name_list = [name['name'] for name in names]
    if len(name_list) == 0:
        return ''
    elif len(name_list) == 1:
        return name_list[0]
    else:
        return ', '.join(name_list[:-1]) + ' & ' + name_list[-1]


assert namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'},
                 {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer & Marge'
assert namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa & Maggie'
assert namelist([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart & Lisa'
assert namelist([{'name': 'Bart'}]) == 'Bart'
assert namelist([]) == ''
