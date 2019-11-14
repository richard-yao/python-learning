"""
@author yaoxs@shukun.net
@date 2019/11/14 10:28
"""


class Test(object):

    def __init__(self, name: str = None, age: int = 0):
        """Test类属性"""
        self.name = name
        self.age = age

    def log_decorator(level):
        print("step in with level: %s" % level)

        def decorator(func):
            """日志装饰器"""
            def wrapper(*args, **kwargs):
                print("%s is running" % func.__name__)
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @log_decorator(level=1)
    def count(self, num1: int, num2: int):
        print("The result of %d + %d = %d" % (num1, num2, (num1 + num2)))