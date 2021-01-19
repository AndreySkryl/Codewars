def solve(a, b):
    return [a.count(item) for item in b]


assert solve(['abc', 'abc', 'xyz', 'abcd', 'cde'], ['abc', 'cde', 'uap']) == [2, 1, 0]
assert solve(['abc', 'xyz', 'abc', 'xyz', 'cde'], ['abc', 'cde', 'xyz']) == [2, 1, 2]
assert solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']) == [2, 0, 1]
