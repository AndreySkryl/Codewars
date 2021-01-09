def set_alarm(employed, vacation):
    return employed and not vacation


assert set_alarm(True, True) == False
assert set_alarm(False, True) == False
assert set_alarm(False, False) == False
assert set_alarm(True, False) == True
