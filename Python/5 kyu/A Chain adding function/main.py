class CustomInt(int):
    def __call__(self, v):
        return CustomInt(self + v)


def add(v):
    return CustomInt(v)


assert add(1) == 1
assert add(1)(2) == 3
assert add(1)(2)(3) == 6
