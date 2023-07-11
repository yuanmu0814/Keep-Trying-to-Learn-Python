# 使用Python语言编写
# 开发时间 2023/7/11 23:39

# 转义字符:
#   反斜杠+想要实现的转义功能首字母
#       换行：\n
#       表示将光标的位置回退到本行的开头位置：\r
#       水平制表符：\t
#       退格：\b

print('hello\nworld')
# 换行
print('hello\tworld')
print('helloooo\tworld')
# | \t |   |   |   | \t |   |   |   | \t |   |   |   |   |
# |----|---|---|---|----|---|---|---|----|---|---|---|---|
# | h  | e | l | l | o  |   |   |   | w  | o | r | l | d |
# | h  | e | l | l | o  | o | o | o | w  | o | r | l | d |
# 制表
print('hello\rworld')
# world把hello进行了覆盖
print('hello\bworld')
# \b是退一个格，将o退没了

print('\\test')
# print('老师说:'大家好'')
print('老师说:\'大家好\'')

# 原字符，不希望字符串中的转义字符起作用，就是用原字符，就是在字符串之前加上r或R
print(r'hello\nworld')
# print(r'hello\nworld\')
# 注意事项：最后一个字符不能是反斜杠

