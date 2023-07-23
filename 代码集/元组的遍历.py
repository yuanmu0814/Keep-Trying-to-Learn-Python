# 使用Python语言编写
# 创建时间 2023/7/21 16:51

# 元组是可迭代对象，所以可以使用for...in进行遍历
t = ('Python', 'world', 98)
print('-----第一种遍历元组元素的方式，使用索引-----')
print(t[0])
print(t[1])
print(t[2])
print('-----第二种遍历元组的方式-----')
for item in t:
    print(item)

