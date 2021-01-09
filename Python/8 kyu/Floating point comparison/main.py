def approx_equals(a, b):
    return abs(a - b) < 0.001


data = (
    (175.9827, 82.25, False),
    (-156.24037, -156.24038, True),
    (123.2345, 123.234501, True),
    (1456.3652, 1456.3641, False),
    (-1.234, -1.233999, True),
    (98.7655, 98.7654999, True),
    (-7.28495, -7.28596, False))


def tests():
    for (a, b, eq) in data:
        print(a, b, eq)
        assert approx_equals(a, b) == eq


tests()
