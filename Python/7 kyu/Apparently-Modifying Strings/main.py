import re


def apparently(string):
    return re.sub(r'\b(and|but)\b(?!\sapparently\s)', r'\1 apparently', f' {string} ').strip()


assert apparently('It was great and I have never been on live television before but sometimes I dont watch this.') == \
       'It was great and apparently I have never been on live television before but apparently sometimes ' \
       'I dont watch this.'
assert apparently('and') == 'and apparently'
assert apparently('apparently') == 'apparently'
