import re
from collections import defaultdict


def simplify(poly):
    groups = re.findall(r'(\+|-)?(\d+)?(\w+)', poly)
    variables = defaultdict(list)
    for group in groups:
        sign, coefficient, variable = group[0], group[1], group[2]
        sorted_variable = ''.join(sorted(variable))

        if not coefficient:
            coefficient = '1'

        variables[sorted_variable].append(int(f'{sign}{coefficient}'))

    accumulated_variables = defaultdict(int)
    for variable in variables:
        summa = sum(variables[variable])
        if summa != 0:
            accumulated_variables[variable] = summa

    result_string = ''
    for item in sorted(accumulated_variables.keys(), key=lambda x: (len(x), x)):
        groups = re.search(r'(\+|-)?(\d+)', str(accumulated_variables[item]))
        sign, coefficient = groups.group(1), groups.group(2)
        if sign is None:
            sign = '+'
        if coefficient == '1':
            coefficient = ''
        result_string += f'{sign}{coefficient}{item}'

    if result_string[0] == '+':
        result_string = result_string[1:]

    return result_string


assert simplify("dc+dcba") == "cd+abcd"
assert simplify("2xy-yx") == "xy"
assert simplify("-a+5ab+3a-c-2a") == "-c+5ab"
assert simplify("-abc+3a+2ac") == "3a+2ac-abc"
assert simplify("xyz-xz") == "-xz+xyz"
assert simplify("a+ca-ab") == "a-ab+ac"
assert simplify("xzy+zby") == "byz+xyz"
assert simplify("-y+x") == "x-y"
assert simplify("y-x") == "-x+y"
