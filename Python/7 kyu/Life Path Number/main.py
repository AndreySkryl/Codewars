import re


def life_path_number(birthdate):
    result = re.findall(r'(\d+)-(\d+)-(\d+)', birthdate)
    year, month, day = result[0]
    life_number = year + month + day
    while len(life_number) != 1:
        life_number = str(sum(int(c) for c in life_number))
    return int(life_number)


assert life_path_number("1955-10-28") == 4
assert life_path_number("1971-06-28") == 7
