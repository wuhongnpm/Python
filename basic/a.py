"""
将华氏温度转换为摄氏温度
"""
f = float(input('请输入华式温度:'))
c = (f -32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f ,c))

"""
输入年份 如果是闰年输出True 否则输出False
"""
year = int(input('请输入年份:'))
is_leap = (year % 4 == 0 and year % 100 != 0 ) or year % 400 ==0
print(is_leap)