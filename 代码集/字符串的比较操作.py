# 使用Python语言编写
# 创建时间 2023/7/26 16:19

# 字符串的比较操作
#   - 运算符：`>`, `>=`, `<=`, `==`, `!=`
#   - 比较规则：首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，两个字符串中的后续字符将不再被比较
#   - 比较原理：两个字符进行比较时，比较的是其ordinal value（原始值），调用内置函数ord可以得到指定字符的ordinal value。与内置函数ord对应的是内置函数chr，调用内置函数chr时指定ordinal value可以得到其对应的字符

print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'), ord('b'))
print(ord('袁'))
print(chr(97), chr(98))
print(chr(34945))
# ==与is的区别：
# ==比较的是value
# is 比较的是id是否相等
a = b = 'Python'
c = 'Python'
print(a == b)
print(a == c)
print(a is b)
print(a is c)
print('a:', id(a))
print('b:', id(b))
print('c:', id(c))


