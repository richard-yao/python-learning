# -*- coding: utf-8 -*-

"""
@author yaoxs@shukun.net
@date 2019/11/19 15:04
"""
from functools import reduce

DiGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}


def using_map_reduce(_str: str):
    def char2num(s):
        return DiGITS[s]

    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(char2num, _str))


result = using_map_reduce('12345')
print(result == 12345)