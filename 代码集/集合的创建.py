# 使用Python语言编写
# 创建时间 2023/7/21 16:51

# 集合的创建方式
#   - 直接{}
#   - 使用内置函数set()
s = {2, 3, 4, 5, 5, 6, 7}
print(s)
print('-----第二种创建方式-----')
s_1 = set(range(5))
print(s_1, type(s_1))
s_2 = set([1, 2, 3, 4, 5])
s_3 = set([1, 2, 3, 3, 4, 4, 5])
print(s_2, type(s_2))
print(s_3, type(s_3))
s_4 = set((1, 2, 3, 4, 4, 'Python', 'Python'))
print(s_4)
s_5 = set('Python')
print(s_5, type(s_5))
print(set())
