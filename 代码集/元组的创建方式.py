# 使用Python语言编写
# 创建时间 2023/7/21 16:50

# 元组的创建方式
#   - 直接小括号
#   - 使用内置函数tuple()
#   - **只包含一个元祖的元素需要使用逗号和小括号**

print('-----第一种，使用()-----')
t_1 = ('Python', 'world', 98)
print(t_1)
print(type(t_1))
print('-----第二种，使用内置函数tuple()-----')
t_2 = tuple(('Python', 'world', 98))
print(t_2)
print(type(t_2))
t_3 = 'Python'
print(t_3, type(t_3))
t_3 = ('Python', )
print(t_3, type(t_3))
print('-----空列表的创建方式-----')
lst_1 = []
lst_2 = list()
print('-----空字典的创建方式-----')
d_1 = {}
d_2 = dict()
print('-----空元组的创建方式-----')
t_4 = ()
t_5 = tuple()

print('空列表', lst_1, lst_2)
print('空字典', d_1, d_2)
print('空元组', t_4, t_5)



