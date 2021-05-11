def validate(username, password):
    if len(username) == 0 or len(password) == 0:
        return False
    for start in range(len(password)):
        for end in range(len(password) + 1):
            if start < end and end - start >= min(len(username), len(password)) // 2:
                substring = password[start:end]
                if substring in username:
                    return False
    return True


assert validate("", "") == False
assert validate("username", "myname") == False
assert validate("sword", "password" ) == False
assert validate("qwertyuiop", "asdfghjkl") == True
assert validate("MASH", "M*A*S*H") == True
assert validate("asdfghjkl", "lkjhgfdsa") == True
