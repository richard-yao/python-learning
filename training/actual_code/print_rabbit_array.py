"""
@author yaoxs@shukun.net
@date 2019/10/10 17:51
"""
count = int(input("请输入需要生成的斐波那契数列数量："))
first_number = 1
print(first_number)
second_number = 1
print(second_number)
now_number = 0
while count > 2:
    count -= 1
    now_number = first_number + second_number
    print(now_number)
    first_number = second_number
    second_number = now_number

