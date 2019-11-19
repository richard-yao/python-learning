# -*- coding: utf-8 -*-

"""
@author yaoxs@shukun.net
@date 2019/11/19 15:56
"""

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(_elm):
    if isinstance(_elm, tuple):
        return _elm[0]
    else:
        return _elm


def by_score(_elm):
    if isinstance(_elm, tuple):
        return _elm[1]
    else:
        return _elm


L2 = sorted(L, key=by_name)
for e in L2:
    print(e)
print('\n')
L3 = sorted(L, key=by_score)
for e in L3:
    print(e)

