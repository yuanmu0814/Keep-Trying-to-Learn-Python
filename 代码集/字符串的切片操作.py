# 使用Python语言编写
# 创建时间 2023/7/26 19:42

# 字符串的切片操作
# 字符串是不可变类型
#   - 不具备增、删、改等操作
#   - 切片操作将产生新的对象
print('切片[start:end:step]')
s = 'hello, Python'
s1 = s[:5]
print(s1)
s2 = s[6:]
print(s2)
new_str = s1 + s2
print(new_str)
print(s[1:5:1])
print((s[::2]))
print(s[::-1])
