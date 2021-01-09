def position(alphabet):
    index = sorted('qwertyuiopasdfghjklzxcvbnm').index(alphabet) + 1
    return f'Position of alphabet: {index}'


tests = [
    ["a", "Position of alphabet: 1"],
    ["z", "Position of alphabet: 26"],
    ["e", "Position of alphabet: 5"],
]

for inp, exp in tests:
    assert position(inp) == exp
