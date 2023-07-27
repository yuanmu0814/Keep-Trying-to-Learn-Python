# 使用Python语言编写
# 创建时间 2023/7/26 20:59

# 字符串的编码转换
# 编码与解码的方式
#   - 编码：将字符串转换为二进制数据（bytes）
#   - 解码：将bytes类型的数据转换为字符串类型
print('-----编码-----')
s = '天涯共此时'
print(s.encode(encoding='GBK'))  # GBK中一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8这种编辑格式中，一个中文占三个字节
print('-----解码-----')
print('byte代表的就是一个二进制数据（字节类型的数据）')
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
