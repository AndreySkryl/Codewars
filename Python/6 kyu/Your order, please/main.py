import re


def order(sentence):
    matches = re.findall(r'(\w*(\d+)\w*)', sentence)
    return ' '.join(map(lambda item: item[0], sorted(matches, key=lambda item: int(item[1]))))


assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
assert order("") == ""
