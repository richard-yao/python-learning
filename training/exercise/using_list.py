"""
@author yaoxs@shukun.net
@date 2019/10/11 14:15
"""
import sys


def using_list_func():
    fruits = ["grape", "apple", "strawberry", "waxberry"]
    print(fruits)
    fruits5 = fruits[::-1]
    print(fruits5)
    print(sorted(fruits))


def using_generate_list():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)


def generate_language():
    f = [x ** 2 for x in range(1, 1000)]
    print("生成式占用内存: %d" % sys.getsizeof(f))
    print("生成式数据：", f)
    f = (x ** 2 for x in range(1, 1000))
    print("生成器占用内存: %d" % sys.getsizeof(f))
    print("生成器数据：", f)
    for val in f:
        print(val, end=" ")


def fib(n):
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == "__main__":
    using_list_func()
    using_generate_list()
    generate_language()
    main()