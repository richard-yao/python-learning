# -*- coding: utf-8 -*-

"""
@author yaoxs@shukun.net
@date 2019/11/19 18:44
"""
import time
import functools


def log(text):
    def decorator(func):

        @functools.wraps(func)
        def wrap(*args, **kw):
            start_time = time.time()
            print('call %s' % func.__name__)
            time.sleep(1)
            value = func(*args, **kw)
            end_time = time.time()
            print('execute time: %s' % (end_time - start_time))
            return value
        return wrap
    return decorator


@log("execute")
def now():
    print('execute function with wrapper')


now()