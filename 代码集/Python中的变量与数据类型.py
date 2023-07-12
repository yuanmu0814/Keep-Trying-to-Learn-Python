# 使用Python语言编写
# 开发时间 2023/7/12 19:17

# 一、变量的定义和使用
# 变量是内存中一个带标签的盒子，用户将需要的数据存入其中

# 变量由三部分组成
# 1.标识：表示对象所存储的内存地址，使用内置函数id(obj)来获取
# 2.类型：表示的是对象的数据类型，使用内置函数type(obj)来获取
# 3.值：表示对象所存储的具体数据，使用print(obj)可以将值进行打印输出

name = 'test_1'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)

# name[**********]

# id **********
# type str
# value test

# 二、变量的多次赋值
# 当多次赋值之后，变量名会指向新的空间
print(name)
name = 'test_2'
print(name)

# 三、Python中常见的数据类型
#   整数类型    int 98
#   浮点数类型   float   3.1415
#   布尔类型    bool    True/False
#   字符串类型   str ‘Python’

# 四、数据类型
# 1.整数类型
# 英文为integer，简写为int，可以表示正数、负数和零
# 整数的不同进制表示方式
#   二进制Binary->以0b为开头
#   八进制Octal->以0o为开头
#   十进制Decimal->默认的进制
#   十六进制Hexadecimal->以0x开头
n1 = 90
n2 = -76
n3 = 0
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))
# 整数可以表示为二进制、八进制、十进制、十六进制
print('二进制', 0b1110110)
print('八进制', 0o166)
print('十进制', 118)
print('十六进制', 0x76)
# 2.浮点类型
# 由整数部分和小数部分组成
a = 3.14159
print(a, type(a))
# 浮点数存储不精确性：使用浮点数进行计算时，可能会出现小数位数不确定的情况
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1+n2)
print(n1+n3)
# 解决方案：导入模块decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
# 3.布尔类型
# boolean
# 用来表示真或假的值
# True表示真，False表示假
# 布尔值可以转化为整数
# True  ->  1
# False ->  0
f1 = True
f2 = False
print(f1, type(f1))
print(f2, type(f2))
# 布尔值可以转为整数计算
print(f1+1, type(f1+1))
print(f2+1, type(f2+1))
# 4.字符串类型
# 字符串类型又被称为不可变的字符序列
# 可以使用单引号‘’，双引号“”，三引号’‘’ ‘’‘或“”“ ”“”来定义
# 单引号和双引号定义的字符串必须在一行
# 三引号定义的字符串可以分布在连续的多行
str1 = 'test_1'
print(str1, type(str1))
str2 = "test_2"
print(str2, type(str2))
str3 = '''test_3_line_1
test_3_line_2'''
str4 = """test_4_line_1
test_4_line_2"""
print(str3, type(str3))
print(str4, type(str4))
# 五、类型转换
# 1.str()函数
name = '张三'
age = 20
print(type(name), type(age))
print('我叫'+name+',今年'+str(age)+'岁')
print('-------------str()将其他类型转成str类型-------------')
a = 10
b = 198.8
c = False
print(type(a), type(b), type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))
# 2.int()函数
print('-------------int()将其他类型转成int类型-------------')
s1 = '128'
f1 = 98.7
s2 = "76.77"
ff = True
s3 = 'hello'
print(type(s1), type(f1), type(s2), type(ff), type(ff), type(s3))
print(int(s1), type(int(s1)))
# 将str转成int类型，字符串为数字串
print(int(f1), type(int(f1)))
# 将float转成int类型，截取整数，舍去小数部分
print(int(s2), type(int(s2)))
# 报错！原因：将str转成int类型，因为字符串为小数串
print(int(ff), type(int(ff)))
print(int(s3), type(int(s3)))
# 报错！原因：将str转成int类型，字符串必须为数字串（且必须为整数），非数字串不允许转换
# 3.float()函数
print('-------------float()将其他类型转成float类型-------------')
s1 = '128.98'
s2 = "76"
ff = True
s3 = 'hello'
i = 98
print(type(s1), type(s2), type(ff), type(s3), type(i))
print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
print(float(ff), type(float(ff)))
print(float(s3), type(float(s3)))
# 报错！原因：字符串中的数据如果是非数字串，则不允许转换
print(float(i), type(float(i)))

