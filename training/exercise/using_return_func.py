# -*- coding: utf-8 -*-

"""
@author yaoxs@shukun.net
@date 2019/11/19 18:13
"""


def lazy_sum(*args):
    def _sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return _sum


def _count():
    """
    闭包特性，这里计算返回的都会是被改变后的同一个局部变量的值
    原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3
    """
    fs = []
    for i in range(1, 4):
        def _f():
            return i * i
        fs.append(_f)
    return fs


def _count_exec():
    """
    这里虽然也是闭包，但是返回的引用函数中已经包括了具体的参数i
    :return:
    """
    def _f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(_f(i))
    return fs


f = lazy_sum(1, 2, 3, 5)
print(f())
f1, f2, f3 = _count()
print(f1())
print('values: %d , %d, %d' % (f1(), f2(), f3()))
f1, f2, f3 = _count_exec()
print(f1())
print('values: %d , %d, %d' % (f1(), f2(), f3()))