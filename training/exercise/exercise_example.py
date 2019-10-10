"""
@author yaoxs@shukun.net
@date 2019/10/10 15:03
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i * j), end="\t")
    print()