import re

operators = {
   '+': 'Plus', '-': 'Minus',
   '*': 'Times', '/': 'Divided By',
   '**': 'To The Power Of',
   '=': 'Equals', '!=': 'Does Not Equal'
}

numbers = '# One Two Three Four Five Six Seven Eight Nine Ten'.split()


def expression_out(exp):
    matches = re.match(r'(\d+) (.+) (\d+)', exp)
    if matches:
        number_1, operator, number_2 = matches.groups()
        number_1, number_2 = [numbers[int(i)] for i in [number_1, number_2]]
        if operator in operators:
            operator = operators[operator]
            return f'{number_1} {operator} {number_2}'
        else:
            return "That's not an operator!"


assert expression_out('1 + 3') == 'One Plus Three'
assert expression_out('2 - 10') == 'Two Minus Ten'
assert expression_out('6 ** 9') == 'Six To The Power Of Nine'
assert expression_out('5 = 5') == 'Five Equals Five'
assert expression_out('7 * 4') == 'Seven Times Four'
assert expression_out('2 / 2') == 'Two Divided By Two'
assert expression_out('8 != 5') == 'Eight Does Not Equal Five'
