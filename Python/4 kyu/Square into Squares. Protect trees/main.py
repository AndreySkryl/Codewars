import math


def decompose_in_sqr(n, i):
    if n == i*i:
        return [i]
    elif i != 1:
        for j in range(i, 0, -1):
            result = [j]
            result.extend(decompose_in_sqr(n - j*j, int(math.sqrt(n - j*j))))
            if sum([x**2 for x in set(result)]) == n:
                return set(result)
        return []
    return []


def decompose(n):
    for i in range(n - 1, 0, -1):
        result = [i]
        result.extend(decompose_in_sqr(n*n - i*i, int(math.sqrt(n*n - i*i))))
        if sum([x**2 for x in set(result)]) == n*n:
            return sorted(set(result))


assert decompose(5) == [3, 4]
assert decompose(8) is None
assert decompose(50) == [1, 3, 5, 8, 49]
