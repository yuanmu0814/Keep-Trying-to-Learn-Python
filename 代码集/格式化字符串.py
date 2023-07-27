# 使用Python语言编写
# 创建时间 2023/7/26 20:15

# 格式化字符串
# 格式化字符串的两种方式
#   - %作占位符
#   - {}作占位符
print('-----%-----')
name = '张三'
age = 20
print('我叫%s，今年%d岁' % (name, age))
print('-----{}-----')
print('我叫{0}，今年{1}岁'.format(name, age))
print('-----f-string-----')
print(f'我叫{name}，今年{age}岁')
print('----------')
print('%10d' % 99)
print('%.3f' % 3.1415926)
print('%10.3f' % 3.1415926)
print('{0}'.format(3.1415926))
print('{0:.3f}'.format(3.1415926))
print('{:10.3f}'.format(3.1415926))
print('0123456789')


