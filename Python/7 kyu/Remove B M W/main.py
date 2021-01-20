import re


def remove_bmw(string):
    if not isinstance(string, str):
        raise TypeError("This program only works for text.")
    return re.sub(r'[bmw]', '', string, flags=re.IGNORECASE)


assert remove_bmw("bmwvolvoBMW") == "volvo"
assert remove_bmw("blablahblah") == "lalahlah"
