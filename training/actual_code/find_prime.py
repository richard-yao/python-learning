"""
@author yaoxs@shukun.net
@date 2019/10/10 18:13
"""
max_number = int(input("请输入搜索的最大值上限: "))
for temp in range(2, max_number):
    is_prime = True
    for x in range(1, temp):
        if temp % x == 0 and x > 1:
            is_prime = False
            break
    if is_prime:
        print("素数：%d" % temp)