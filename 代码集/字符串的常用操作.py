# 使用Python语言编写
# 创建时间 2023/7/25 18:51

# 字符串的常用操作
# 字符串的查询操作的方法
# | 功能   | 方法名称     | 作用                                            |
# |:------|:----------|:-----------------------------------------------|
# | 查询方法 | index()  | 查找子串substr第一次出现的位置，如果查找的子串不存在，则抛出ValueError   |
# | 查询方法 | rindex() | 查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError |
# | 查询方法 | find()   | 查找子串substr第一次出现的位置，如果查找的子串不存在时，则返回-1          |
# | 查询方法 | rfind()  | 查找子串substr最后一次出现的位置，如果查找的子串不存在时，则返回-1         |

s = 'hello, hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))
# print(s.index('k'))  ValueError: substring not found
print(s.find('k'))
# print(s.rindex('k'))  ValueError: substring not found
print(s.rfind('k'))


# 字符串的大小写转换操作的方法
# | 功能    | 方法名称         | 作用                               |
# |:-------|:--------------|:----------------------------------|
# | 大小写转换 | upper()      | 把字符串中所有字符都转成大写字母                 |
# | 大小写转换 | lower()      | 把字符串中所有字符都转成小写字母                 |
# | 大小写转换 | swapcase()   | 把字符串中所以大写字母转成小写字母，把所以小写字母都转成大写字母 |
# | 大小写转换 | capitalize() | 把第一个字符转换成大写，把其余字符转换为小写           |
# | 大小写转换 | title()      | 把每个单词的第一个字符转换成大写，把每个单词的剩余字符转换为小写 |

s = 'hello, python'
print(s, id(s))
print(s.upper(), id(s.upper()))
print(s.lower(), id(s.lower()))

s2 = 'hello, Python'
print(s2.swapcase())
print(s2.title())


# 字符串内容对齐操作的方法
# | 功能    | 方法名称     | 作用                                                            |
# |-------|----------|---------------------------------------------------------------|
# | 字符串对齐 | center() | 居中对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串 |
# | 字符串对齐 | ljust()  | 左对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串  |
# | 字符串对齐 | rjust()  | 右对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串  |
# | 字符串对齐 | zfill    | 右对齐，左边用0填充，该方法只接受一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身    |

s = 'hello,Python'
print(s.center(20, '*'))
print(s.ljust(20, '*'))
print(s.ljust(10))
print(s.rjust(20))
print(s.zfill(20))
print('-8910'.zfill(8))

# 字符串劈分操作的方法
# | 功能     | 方法名称     | 作用                                                   |
# |--------|----------|------------------------------------------------------|
# | 字符串的劈分 | split()  | 从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表                 |
# | 字符串的劈分 | split()  | 以通过参数sep指定劈分字符串时的劈分符                                 |
# | 字符串的劈分 | split()  | 通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分 |
# | 字符串的劈分 | rsplit() | 从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表                 |
# | 字符串的劈分 | rsplit() | 以通过参数sep指定劈分字符串时的劈分符                                 |
# | 字符串的劈分 | rsplit() | 通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分 |

s = 'hello world python'
lst = s.split()
print(lst)
s1 = 'hello|world|Python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))
print('-----------')
print(s.rsplit())
print(s.rsplit(sep='|'))
print(s.rsplit(sep='|', maxsplit=1))

# 判断字符串操作的方法
# | 功能       | 方法名称           | 作用                               |
# |----------|----------------|----------------------------------|
# | 判断字符串的方法 | isidentifier() | 判断指定的字符串是不是合法的标识符                |
# | 判断字符串的方法 | isspace()      | 判断指定的字符串是否全部由空白字符组成（回车、换行，水平制表符） |
# | 判断字符串的方法 | isalpha()      | 判断指定的字符串是否全部由字母组成                |
# | 判断字符串的方法 | isdecimal()    | 判断指定字符串是否全部由十进制的数字组成             |
# | 判断字符串的方法 | isnumeric()    | 判断指定字符串是否全部由数字组成                 |
# | 判断字符串的方法 | isalnum()      | 判断指定字符串是否全部由字母和数字组成              |

s = 'hello, python'
print('1.', s.isidentifier())
print('2.', 'hello'.isidentifier())
print('3.', '张三'.isidentifier())
print('4.', '张三_123'.isidentifier())
print('5.', '\t'.isspace())
print('6.', 'abc'.isalpha())
print('7.', '张三'.isalpha())
print('8.', '张三1'.isalpha())
print('9.', '123'.isdecimal())
print('10.', '123四'.isdecimal())
print('11.', 'II III'.isdecimal())
print('12.', '123'.isnumeric())
print('13.', '123四'.isnumeric())
print('14.', 'ⅢⅦ四拾'.isnumeric())
print('15.', 'abcd'.isalnum())
print('15.', '张三123'.isalnum())
print('15.', '张三123'.encode('utf-8').isalnum())
print('16.', 'abc!'.isalnum())

# 字符串操作的其他方法
# | 功能     | 方法名称      | 作用                                                                                |
# |--------|-----------|-----------------------------------------------------------------------------------|
# | 字符串替换  | replace() | 第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，该方法返回替换后得到的字符串，替换前的字符串不发生变化，调用该方式时可以通过第三个参数指定最大替换次数 |
# | 字符串的合并 | join()    | 将列表或元组中的字符串合并成一个字符串                                                               |

s = 'hello, Python'
print(s.replace('Python', 'Java'))
s1 = 'hello, Python, Python, Python'
print(s1.replace('Python', 'Java', 2))

lst = ['hello', 'Java', 'Python']
print('|'.join(lst))
print(''.join(lst))
print('&'.join('Python'))
