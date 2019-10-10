"""
@author yaoxs@shukun.net
@date 2019/10/10 14:25
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input("请输入: "))
    if number < answer:
        print("猜小了")
    elif number > answer:
        print("猜大了")
    else:
        print("恭喜找到正确结果")
        break
print("你总共猜了%d次" % counter)
if counter > 7:
    print("你这猜的太烂了!")

