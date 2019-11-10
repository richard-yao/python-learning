"""
@author yaoxs
@date 2019/11/10 17:56
"""

'''
生成斐波那契数列
'''


def generate_fib_seq(number):
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


if __name__ == '__main__':
    generate_fib_seq(20)
