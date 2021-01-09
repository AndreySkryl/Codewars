def abbrev_name(name):
    return '.'.join(string[0].upper() for string in name.split())


assert abbrev_name("Sam Harris") == "S.H"
assert abbrev_name("Patrick Feenan") == "P.F"
assert abbrev_name("Evan Cole") == "E.C"
assert abbrev_name("P Favuzzi") == "P.F"
assert abbrev_name("David Mendieta") == "D.M"
