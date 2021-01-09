def people_with_age_drink(age):
    drink = ''
    if age < 14:
        drink = 'toddy'
    elif age < 18:
        drink = 'coke'
    elif age < 21:
        drink = 'beer'
    else:
        drink = 'whisky'
    return f'drink {drink}'


assert people_with_age_drink(13) == 'drink toddy'
assert people_with_age_drink(0) == 'drink toddy'
assert people_with_age_drink(17) == 'drink coke'
assert people_with_age_drink(15) == 'drink coke'
assert people_with_age_drink(14) == 'drink coke'
assert people_with_age_drink(20) == 'drink beer'
assert people_with_age_drink(18) == 'drink beer'
assert people_with_age_drink(22) == 'drink whisky'
assert people_with_age_drink(21) == 'drink whisky'
