import math
from string import ascii_lowercase, ascii_uppercase, ascii_letters


def modify_char(char, shift):
    if char not in ascii_letters:
        return char

    letters = ascii_lowercase if char in ascii_lowercase else ascii_uppercase
    return letters[(letters.index(char) + shift) % len(letters)]


def encode_str(strng, shift):
    prefix = strng[0].lower() + modify_char(strng[0].lower(), shift)
    result = prefix + ''.join([modify_char(c, shift) for c in strng])

    delta = math.ceil(len(result) / 5)
    splits = [result[i:i+delta] for i in range(0, len(result), delta)]
    return splits


def decode(array):
    string = ''.join(array)
    prefix = string[:2]
    shift = ord(prefix[1]) - ord(prefix[0]) if ord(prefix[0]) <= ord(prefix[1]) \
        else -abs(ord(prefix[0]) - ord(prefix[1]))
    source_string = ''.join([modify_char(c, -shift) for c in string[2:]])
    return source_string


def testing_code(strng, shift, exp):
    actual = encode_str(strng, shift)
    assert actual == exp


def testing_decode(arr, exp):
    actual = decode(arr)
    assert actual == exp


def tests1():
    u = "I should have known that you would have a perfect answer for me!!!"
    v = ["ijJ tipvme ibw", "f lopxo uibu z", "pv xpvme ibwf ", "b qfsgfdu botx", "fs gps nf!!!"]
    testing_code(u, 1, v)
    v = ['ikK ujqwnf jcx', 'g mpqyp vjcv a', 'qw yqwnf jcxg ', 'c rgthgev cpuy', 'gt hqt og!!!']
    testing_code(u, 28, v)

    u = "abcdefghjuty12"
    v = ['abbc', 'defg', 'hikv', 'uz12']
    testing_code(u, 1, v)
    v = ['aeef', 'ghij', 'klny', 'xc12']
    testing_code(u, 30, v)


def tests2():
    u = "O CAPTAIN! my Captain! our fearful trip is done;"
    v = ["opP DBQUBJ", "O! nz Dbqu", "bjo! pvs g", "fbsgvm usj", "q jt epof;"]
    testing_decode(v, u)
    v = ['owW KIXBIQ', 'V! ug Kixb', 'iqv! wcz n', 'miznct bzq', 'x qa lwvm;']
    testing_decode(v, u)

    u = "Exult, O shores, and ring, O bells! But I, with mournful tread, Walk the deck my Captain lies, Fallen cold " \
        "and dead. "
    v = ["efFyvmu, P tipsft, boe s", "joh, P cfmmt! Cvu J, xju", "i npvsogvm usfbe, Xbml u",
         "if efdl nz Dbqubjo mjft,", " Gbmmfo dpme boe efbe. "]
    testing_decode(v, u)


tests1()
tests2()
