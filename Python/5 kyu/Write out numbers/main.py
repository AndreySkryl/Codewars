words = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen ' \
        'seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety '.split()


def number2words(n: int):
    """ works for numbers between 0 and 999999 """
    global words
    if n < 20:
        return words[n]
    if n < 100:
        return words[18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10])
    if n < 1000:
        return number2words(n // 100) + ' hundred' + ('' if n % 100 == 0 else ' ' + number2words(n % 100))
    if n < 1000000:
        return number2words(n // 1000) + ' thousand' + ('' if n % 1000 == 0 else ' ' + number2words(n % 1000))


assert number2words(0) == "zero"
assert number2words(1) == "one"
assert number2words(8) == "eight"
assert number2words(10) == "ten"
assert number2words(19) == "nineteen"
assert number2words(20) == "twenty"
assert number2words(22) == "twenty-two"
assert number2words(54) == "fifty-four"
assert number2words(80) == "eighty"
assert number2words(98) == "ninety-eight"
assert number2words(100) == "one hundred"
assert number2words(301) == "three hundred one"
assert number2words(793) == "seven hundred ninety-three"
assert number2words(800) == "eight hundred"
assert number2words(650) == "six hundred fifty"
assert number2words(1000) == "one thousand"
assert number2words(1003) == "one thousand three"
