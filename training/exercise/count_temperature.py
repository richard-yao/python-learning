"""
@author yaoxs@shukun.net
@date 2019/10/9 10:19
"""
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
'''这里在print中使用%来表示后面接的是占位符参数'''
print('%.1f华氏度 = %.1f摄氏度' % (f, c))