"""
@author yaoxs@shukun.net
@date 2019/10/10 17:51
"""


def generate_rabbit_array(count=2):
    array = []
    first_number = 1
    array.append(first_number)
    second_number = 1
    array.append(second_number)
    now_number = 0
    while count > 2:
        count -= 1
        now_number = first_number + second_number
        array.append(now_number)
        first_number = second_number
        second_number = now_number
    return array


def main():
    count = int(input("请输入需要生成的斐波那契数列数量："))
    for value in generate_rabbit_array(count):
        print(value)


if __name__ == '__main__':
    main()