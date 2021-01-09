def derive(coefficient, exponent):
    return str(coefficient * exponent) + f'x^{exponent - 1}' if exponent - 1 > 1 else ''


assert derive(7, 8) == "56x^7"
assert derive(5, 9) == "45x^8"
