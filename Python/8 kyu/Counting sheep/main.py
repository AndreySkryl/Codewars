def count_sheeps(sheeps):
    return sheeps.count(True)


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True];

assert count_sheeps(array1) == 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1)
