# 使用Python语言编写
# 创建时间 2023/7/23 21:02

# 集合的数学操作
# - 交集
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)
print(s1, s2)

# - 并集
print(s1.union(s2))
print(s1 | s2)
print(s1, s2)

# - 差集
print(s1.difference(s2))
print(s1 - s2)
print(s1, s2)

# - 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
