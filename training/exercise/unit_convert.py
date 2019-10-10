"""
@author yaoxs@shukun.net
@date 2019/10/9 16:39
"""
value = float(input("请输入长度: "))
unit = input("请输入单位: ")
if unit == "in" or unit == "英寸":
    print("%.3f英寸 = %.3f厘米" % (value, value * 2.54))
elif unit == "cm" or unit == '厘米':
    print("%.3f厘米 = %.3f英寸" % (value, value / 2.54))
else:
    print("请输入有效的单位")