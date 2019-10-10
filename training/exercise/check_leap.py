"""
@author yaoxs@shukun.net
@date 2019/10/9 11:07
"""
year = int(input("请输入年份："))
is_leap = (year % 4 == 0 and year % 100 != 0) \
    or year % 400 == 0
print("%d " % year, is_leap)