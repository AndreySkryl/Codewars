# TODO : пересмотреть
# def who_is_next(names, r):
#     calculation = True
#     start, end, i = 1, 0, 0.5
#     while calculation:
#         i *= 2
#         end += i * len(names)
#         if r <= end:
#             step_back = (i * len(names)) // len(names)
#             for index in range(len(names)):
#                 end -= step_back
#                 if r > end:
#                     return names[-(index + 1)]
#             calculation = False
#     return None

def who_is_next(names, r):
    index = r - 1
    l_names = len(names)

    while index >= l_names:
        # skip the beginning and de-duplicate pairs, e.g.:
        # 'abcaabbcc'[5] == 'aabbcc'[5 - 3] == 'abc'[(5 - 3) // 2]
        index = (index - l_names) // 2

    return names[index]


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

assert who_is_next(names, 1) == "Sheldon"
assert who_is_next(names, 52) == "Penny"
assert who_is_next(names, 7230702951) == "Leonard"
