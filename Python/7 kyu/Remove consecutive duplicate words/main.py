from itertools import groupby


def remove_consecutive_duplicates(s):
    return ' '.join(k for k, g in groupby(s.split()))


assert remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta') == 'alpha beta gamma delta alpha beta gamma delta'
assert remove_consecutive_duplicates('aa a aa a aa') == 'aa a aa a aa'
assert remove_consecutive_duplicates('this his is sih siht') == 'this his is sih siht'
