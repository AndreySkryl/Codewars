def uncensor(infected, discovered):
    return infected.replace('*', '{}').format(*discovered)


def example_fixed():
    data = [
        ('*h*s *s v*ry *tr*ng*', 'Tiiesae', 'This is very strange'),
        ('A**Z*N*', 'MAIG', 'AMAZING'),
        ('xyz', '', 'xyz'),
        ('', '', ''),
        ('***', 'abc', 'abc')
    ]

    for infected, discovered, result in data:
        assert uncensor(infected, discovered) == result


example_fixed()
