import re


def check_password(s):
    PATTERN = re.compile(
        '^'
        '(?=.*?[A-Z])'
        '(?=.*?[a-z])'
        '(?=.*?\d)'
        '(?=.*?[!@#$%^&*?])'
        '[A-Za-z\d!@#$%^&*?]'
        '{8,20}'
        '$'
    )
    return 'valid' if PATTERN.match(s) else 'not valid'


assert check_password("") == "not valid"
assert check_password("password") == "not valid"
assert check_password("P1@p") == "not valid"
assert check_password("P1@pP1@p") == "valid"
assert check_password("P1@pP1@pP1@pP1@pP1@pP1@p") == "not valid"
assert check_password("Paaaaaa222!!!") == "valid"
