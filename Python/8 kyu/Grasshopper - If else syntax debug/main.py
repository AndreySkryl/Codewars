def check_alive(health):
    if health <= 0:
        return False
    else:
        return True


assert check_alive(-2) == False
assert check_alive(0) == False
assert check_alive(1) == True
assert check_alive(3) == True
