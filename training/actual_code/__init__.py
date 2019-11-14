"""
@author yaoxs@shukun.net
@date 2019/11/14 10:36
"""
from training.actual_code.use_decorator import Test


def execute():
    """test using decorator"""
    test = Test()
    test.count(21, 23)


if __name__ == "__main__":
    execute()