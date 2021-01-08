from collections import defaultdict


def is_prime(number):
    return 2 in [number, 2 ** number % number]


def prime_factors(number):
    primes = list(filter(is_prime, range(2, int(number ** 0.5) + 1)))
    decompositions = defaultdict(int)
    for prime in primes:
        while number % prime == 0:
            decompositions[prime] += 1
            number //= prime

    if number != 1:
        decompositions[number] += 1

    string = ''.join([
        '({}**{})'.format(value, degree) if degree != 1
        else '({})'.format(value)
        for value, degree in sorted(decompositions.items(), key=lambda item: item[0])
    ])
    return string


assert prime_factors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)"
assert prime_factors(86240) == "(2**5)(5)(7**2)(11)"
print(prime_factors(933555431))
