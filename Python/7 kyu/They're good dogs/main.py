import re


def we_rate_dogs(string, rating):
    return re.sub(r'\d+/', f'{rating}/', string)


assert we_rate_dogs('This is Tucker. He would like a hug. 3/10 someone hug him', 11) == \
       'This is Tucker. He would like a hug. 11/10 someone hug him'
assert we_rate_dogs('This is Charlie. He pouts until he gets to go on the swing. 5/10 manipulative af.', 12) == \
       "This is Charlie. He pouts until he gets to go on the swing. 12/10 manipulative af."
