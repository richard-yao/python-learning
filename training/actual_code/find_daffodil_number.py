"""
@author yaoxs@shukun.net
@date 2019/10/10 17:07
"""
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print("find one %d" % num)