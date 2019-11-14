"""
@author yaoxs@shukun.net
@date 2019/11/14 10:36
"""
from training.actual_code.use_decorator import Test
from training.actual_code import use_decorator


def execute():
    """test using decorator"""
    test = Test()
    # 打印带有装饰器的count方法名
    print("call method %s with result: %s" % (test.count.__name__, test.count(21, 23)))
    print("In python you can access to module variable directly: %d" % use_decorator._GLOBAL_PARAM)


if __name__ == "__main__":
    execute()