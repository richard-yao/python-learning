"""
@author yaoxs
@date 2019/11/10 17:56
"""


def generate_fib_seq(number):
    """生成斐波那契数列"""
    first = 1
    second = 1
    result = [first, second]
    if number <= 2:
        return result
    else:
        for i in range(2, number):
            next_elm = first + second
            first = second
            second = next_elm
            result.append(next_elm)
    print(result)


def perfect_numer(number):
    """查找完美数"""
    result = 1
    if number < 6:
        return 0
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            result += i
    if result == number:
        return number
    else:
        return 0


def find_perfect_numer(max_area):
    """查找完美数"""
    result = []
    for i in range(1, max_area):
        elm = perfect_numer(i)
        if elm > 0:
            result.append(elm)
    print(result)


if __name__ == '__main__':
    generate_fib_seq(20)
    find_perfect_numer(10000)
