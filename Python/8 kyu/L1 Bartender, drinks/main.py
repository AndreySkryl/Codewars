def get_drink_by_profession(param):
    table = {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }
    formatted_param = ' '.join(map(str.capitalize, param.split()))
    return table[formatted_param] if formatted_param in table.keys() else 'Beer'


assert get_drink_by_profession("jabrOni") == "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'"
assert get_drink_by_profession(
    "scHOOl counselor") == "Anything with Alcohol", "'School Counselor' should map to 'Anything with alcohol'"
assert get_drink_by_profession(
    "prOgramMer") == "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'"
assert get_drink_by_profession("bike ganG member") == "Moonshine", "'Bike Gang Member' should map to 'Moonshine'"
assert get_drink_by_profession("poLiTiCian") == "Your tax dollars", "'Politician' should map to 'Your tax dollars'"
assert get_drink_by_profession("rapper") == "Cristal", "'Rapper' should map to 'Cristal'"
assert get_drink_by_profession("pundit") == "Beer", "'Pundit' should map to 'Beer'"
assert get_drink_by_profession("Pug") == "Beer", "'Pug' should map to 'Beer'"
