def check_exam(arr1, arr2):
    points = 0
    for right_answer, student_answer in list(zip(arr1, arr2)):
        if right_answer == student_answer:
            points += 4
        elif student_answer not in [right_answer, '']:
            points -= 1
    return points if points > 0 else 0


assert check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) == 6
assert check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) == 7
assert check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) == 16
assert check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) == 0
