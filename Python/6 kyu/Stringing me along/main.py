def create_message(s):
    return lambda tmp_s=None: s if tmp_s is None else create_message(s + ' ' + tmp_s)


assert create_message("Hello")("World!")("how")("are")("you?")() == "Hello World! how are you?"
