def even_or_odd(number):
    return 'Odd' if number % 2 == 1 else 'Even'


assert even_or_odd(2) == "Even"
assert even_or_odd(1) == "Odd"
assert even_or_odd(0) == "Even"
assert even_or_odd(1545452) == "Even"
assert even_or_odd(7) == "Odd"
assert even_or_odd(78) == "Even"
assert even_or_odd(17) == "Odd"
assert even_or_odd(74156741) == "Odd"
assert even_or_odd(100000) == "Even"
assert even_or_odd(-123) == "Odd"
assert even_or_odd(-456) == "Even"
