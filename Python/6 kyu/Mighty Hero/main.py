def count_of_heads(initial, n, swings):
    result = initial
    coefficient = 1
    for i in range(1, swings+1):
        coefficient *= i
        result = result - 1 + n*coefficient
    return result



assert count_of_heads(2, 1, 1) == 2
assert count_of_heads(5, 10, 3) == 92
assert count_of_heads(5, 10, 2) == 33
assert count_of_heads(51, 6, 31) == 50983496835888389711611599965641898
assert count_of_heads(30, 12, 33) == 107459348462618737087648172161211283753
assert count_of_heads(10, 8, 3) == 79
assert count_of_heads(1, 1, 3) == 7
assert count_of_heads(100, 143, 8) == 6611411
