import re


def triple_x(s):
    matches = re.findall(r'x+', s)
    return len(matches[0]) >= 3 if matches else False


assert triple_x("") == False
assert triple_x("there's no XXX here") == False
assert triple_x("abraxxxas") == True
assert triple_x("xoxotrololololololoxxx") == False
assert triple_x("soft kitty, warm kitty, xxxxx") == True
assert triple_x("softx kitty, warm kitty, xxxxx") == False
