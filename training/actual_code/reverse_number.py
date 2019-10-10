"""
@author yaoxs@shukun.net
@date 2019/10/10 17:36
"""
number = int(input("请输入: "))
reverse_num = 0
while number > 0:
    reverse_num = reverse_num * 10 + number % 10
    number //= 10
print(reverse_num)