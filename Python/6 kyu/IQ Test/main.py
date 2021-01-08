def iq_test(numbers):
    number_list = list(map(int, numbers.split()))
    odds = list(filter(lambda x: x & 1, number_list))
    evens = list(filter(lambda x: x % 2 == 0, number_list))
    to_find = odds[0] if len(odds) < len(evens) else evens[0]
    return number_list.index(to_find) + 1


assert iq_test("2 4 7 8 10") == 3
assert iq_test("1 2 2") == 1
