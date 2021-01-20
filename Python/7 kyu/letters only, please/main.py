import re
from string import ascii_letters


def remove_chars(s):
    return re.sub(rf'[^{ascii_letters}\s]', '', s)


assert remove_chars("test for error!") == "test for error"
assert remove_chars(".tree1") == 'tree'
