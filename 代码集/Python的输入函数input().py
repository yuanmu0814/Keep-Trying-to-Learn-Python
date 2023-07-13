# 使用Python语言编写
# 开发时间 2023/7/13 11:20

# Python的输入函数input()
# input()函数的介绍
# 作用：接受来自用户的输入
# 返回值类型：输入值的类型为str
# 值的存储：使用=对输入的值进行存储
# input()函数的基本使用
present = input('你想要什么礼物呢？')
print(present, type(present))
# input('里面可以填写自己想要出现在屏幕中提示用户的语句')

# input()函数的高级使用
# 从键盘中读入两个整数，计算两个整数的和
a = input('请输入第一个数')
b = input('请输入第二个数')
print(a+b, type(a+b))
# >-输出的是两个str连接
print(int(a)+int(b), type(int(a)+int(b)))
# >-输出的是两个整数的加和
# 同时也可以在读入键盘键入时就进行转换
a = int(input('请输入第一个数'))
b = int(input('请输入第二个数'))
print(a+b, type(a+b))
