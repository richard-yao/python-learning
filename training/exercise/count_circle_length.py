"""
@author yaoxs@shukun.net
@date 2019/10/9 10:24
"""
import math

radius = float(input("请输入圆的半径: "))
perimeter = 2 * math.pi * radius
print("周长：%.2f" % perimeter)
area = math.pi * radius ** 2
print("面积：%.2f" % area)
