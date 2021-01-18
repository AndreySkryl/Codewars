u = [1, 1, 2]


def build_sequence_u(n):
    global u

    start_len = len(u)
    if start_len < n:
        for i in range(start_len, n):
            element = u[i - u[i - 1]] + u[i - u[i - 2]]
            u.append(element)


def length_sup_u_k(n, k):
    global u
    build_sequence_u(n)

    array = list(filter(lambda x: x >= k, u[:n]))
    return len(array)


def comp(n):
    global u
    build_sequence_u(n)

    count = 0
    for i in range(1, len(u[:n])):
        if u[i] < u[i - 1]:
            count += 1
    return count


def dotest1(n, k, res):
    assert length_sup_u_k(n, k) == res


def dotest2(n, res):
    assert comp(n) == res


dotest1(50, 25, 2)
dotest1(3332, 973, 1391)
dotest1(2941, 862, 1246)
dotest1(3177, 573, 2047)
dotest1(1745, 645, 474)

dotest2(74626, 37128)
dotest2(71749, 35692)
dotest2(56890, 28281)
dotest2(60441, 30054)
dotest2(21361, 10581)
