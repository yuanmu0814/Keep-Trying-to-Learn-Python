# 使用Python语言编写
# 开发时间 2023/7/12 19:17

# 变量的定义和使用
# 变量是内存中一个带标签的盒子，用户将需要的数据存入其中

# 变量由三部分组成
# 1.标识：表示对象所存储的内存地址，使用内置函数id(obj)来获取
# 2.类型：表示的是对象的数据类型，使用内置函数type(obj)来获取
# 3.值：表示对象所存储的具体数据，使用print(obj)可以将值进行打印输出

name = 'test'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)

# name[**********]

# id **********
# type str
# value test