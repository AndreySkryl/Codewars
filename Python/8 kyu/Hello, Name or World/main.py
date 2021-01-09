def hello(name=''):
    if not name:
        return 'Hello, World!'
    return f'Hello, {name.capitalize()}!'


tests = (
    ("John", "Hello, John!"),
    ("aLIce", "Hello, Alice!"),
    ("", "Hello, World!"),
)

for inp, exp in tests:
    assert hello(inp) == exp

assert hello() == "Hello, World!"
