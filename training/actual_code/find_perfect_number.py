"""
@author yaoxs@shukun.net
@date 2019/10/10 18:04
"""
max_number = int(input("请输入最大值："))

for x in range(2, max_number):
    total_sum = 0
    for elm in range(1, x):
        if x % elm == 0:
            total_sum += elm
    if total_sum == x:
        print("完美数：%d" % x)