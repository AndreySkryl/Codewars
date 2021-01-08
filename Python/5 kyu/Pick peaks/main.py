def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i]:
            prob_peak = i
        elif arr[i - 1] > arr[i] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos': pos, 'peaks': [arr[i] for i in pos]}

# def pick_peaks(array):
#     if len(array) <= 2:
#         return {'pos': [], 'peaks': []}
#     pos_and_peaks = []
#     current_local_max_pos = None
#     current_local_max = None
#     for i in range(1, len(array) - 1):
#         prev_item, item, next_item = array[i - 1], array[i], array[i + 1]
#
#         if prev_item < item >= next_item:
#             current_local_max_pos = i
#             current_local_max = item
#
#         if prev_item <= item > next_item:
#             if current_local_max_pos is not None and current_local_max is not None:
#                 pos_and_peaks.append((current_local_max_pos, current_local_max))
#
#         pos_and_peaks = sorted(set(pos_and_peaks))
#     return {'pos': [item[0] for item in pos_and_peaks], 'peaks': [item[1] for item in pos_and_peaks]}


assert pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]) == {"pos": [3, 7], "peaks": [6, 3]}
assert pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) == {"pos": [3, 7], "peaks": [6, 3]}
assert pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]) == {"pos": [3, 7, 10], "peaks": [6, 3, 2]}
assert pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]) == {"pos": [2, 4], "peaks": [3, 2]}
assert pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]) == {"pos": [2], "peaks": [3]}
assert pick_peaks([2, 1, 3, 2, 2, 2, 2, 5, 6]) == {"pos": [2], "peaks": [3]}
assert pick_peaks([2, 1, 3, 2, 2, 2, 2, 1]) == {"pos": [2], "peaks": [3]}
assert pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]) == {
    "pos": [2, 7, 14, 20], "peaks": [5, 6, 5, 5]}
assert pick_peaks([]) == {"pos": [], "peaks": []}
assert pick_peaks([1, 1, 1, 1]) == {"pos": [], "peaks": []}
