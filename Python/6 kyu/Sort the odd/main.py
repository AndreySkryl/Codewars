def sort_array(source_array):
    odds = sorted(filter(lambda x: x & 1, source_array), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]


    # odds = list(filter(lambda x: x & 1, source_array))
    # odds.sort()
    # odd_index = 0
    # odd_sorted_array = []
    # for item in source_array:
    #     if item & 1:
    #         odd_sorted_array.append(odds[odd_index])
    #         odd_index += 1
    #     else:
    #         odd_sorted_array.append(item)
    # return odd_sorted_array


assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
assert sort_array([]) == []