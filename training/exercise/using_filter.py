# -*- coding: utf-8 -*-

"""
@author yaoxs@shukun.net
@date 2019/11/19 15:16
"""


def not_empty(s: str):
    return s and s.strip()


def is_odd(n):
    return n % 2 == 1


_list = list(filter(not_empty, ['A', '', 'B', None, 'C']))
for elm in _list:
    print(elm)
_list = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15]))
for elm in _list:
    print(elm)
