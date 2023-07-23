# 使用Python语言编写
# 创建时间 2023/7/23 20:45

# 集合间的关系
# - 两个集合是否相等
#   - 可以使用运算符==或!=进行判断
# - 一个集合是否是另一个集合的子集
#   - 可以调用方法issubset进行判断
# - 一个集合是否是另一个集合的超集
#   - 可以调用方法issuperset进行判断
# - 两个集合是否没有交集
#   - 可以调用方法isdisjoint进行判断

print('两个集合是否相等（元素相同就相等）')
s1 = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s1 == s2)
print(s1 != s2)
print('一个集合是否是另一个集合的子集')
s1 = {10, 20, 30, 40, 50,60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))
print(s3.issubset(s1))
print('一个集合是否是另一个集合的超集')
print(s1.issuperset(s2))
print(s1.issuperset(s3))
print('两个集合是否含有交集')
print(s2.isdisjoint(s3))
