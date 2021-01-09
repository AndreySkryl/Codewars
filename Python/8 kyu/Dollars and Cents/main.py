def format_money(amount):
    return f'${amount:.2f}'


assert format_money(39.99) == '$39.99'
