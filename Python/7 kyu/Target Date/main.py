# import datetime as dt
#
#
# def date_nb_days(a0, a, p):
#     current_date = dt.date(2016, 1, 1)
#     current_a = a0
#     p_per_day = p / 36000
#     while current_a < a:
#         current_a += current_a * p_per_day
#         current_date += dt.timedelta(1)
#     string = current_date.strftime('%Y-%m-%d')
#     return string

from math import log, ceil
from datetime import date, timedelta as td


def date_nb_days(a0, a, p):
    n = log(a, 1 + p/36000.0) - log(a0, 1 + p/36000.0)
    return str(date(2016, 1, 1) + td(ceil(n)))



def testing(actual, expected):
    assert actual == expected


testing(date_nb_days(4281, 5087, 2), "2024-07-03")
testing(date_nb_days(4620, 5188, 2), "2021-09-19")
testing(date_nb_days(9999, 11427, 6), "2018-03-13")
testing(date_nb_days(3525, 4822, 3), "2026-04-18")
testing(date_nb_days(5923, 6465, 6), "2017-06-10")
testing(date_nb_days(4254, 4761, 8), "2017-05-22")
testing(date_nb_days(1244, 2566, 4), "2033-11-04")
testing(date_nb_days(6328, 7517, 5), "2019-05-25")
testing(date_nb_days(2920, 3834, 2), "2029-06-03")
testing(date_nb_days(7792, 8987, 4), "2019-07-09")
