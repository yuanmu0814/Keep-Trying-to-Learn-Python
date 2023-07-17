# 使用Python语言编写
# 创建时间 2023/7/16 16:42

# 列表元素的增加操作
# | 方法/其他   | 操作描述                    |
# |:----------|:---------------------------|
# | append()  | 在列表的末尾添加一个元素（ 无论添加几个，均作为一个添加）|
# | extend()  | 在列表的末尾至少添加一个元素     |
# | insert()  | 在列表的任意位置添加一个元素     |
# | 切片       | 在列表的任意位置添加至少一个元素 |

lst = [10, 20, 30]
print('添加元素之前', lst, id(lst))
lst.append(100)
print('添加元素之后', lst, id(lst))
lst_2 = ['hello', 'world']
lst.append(lst_2)
print(lst, id(lst))
lst.extend(lst_2)
print(lst, id(lst))
lst.insert(1, 90)
print(lst)
lst_3 = [True, False, 'hello']
lst[1::] = lst_3
print(lst)

# 列表元素的删除操作
# | 方法/其他    | 操作描述                |
# |----------|---------------------|
# | remove() | 一次删除一个元素            |
# | remove() | 重复元素只删除第一个          |
# | remove() | 元素不存在抛出ValueError   |
# | pop()    | 删除一个指定索引位置上的元素      |
# | pop()    | 指定索引不存在抛出IndexError |
# | pop()    | 不指定索引，删除列表中最后一个元素   |
# | 切片      | 一次至少删除一个元素          |
# | clear()  | 清空列表                |
# | del      | 删除列表                |
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)
print(lst)
lst.pop(1)
print(lst)
lst.pop()
print(lst)
print('-----产生一个新的列表对象,复制需要的部分-----')
new_list = lst[1: 3:]
print('切片后的列表:', new_list)
print('-----不产生新的列表对象，而是删除原列表中的内容-----')
lst[1: 3:] = []
print(lst)
print('-----清除列表中的所有元素-----')
lst.clear()
print(lst)
print('-----del语句会将列表对象删除-----')
del lst

# 列表元素的修改操作
#   - 为指定的索引的元素赋予一个新值
#   - 为指定的切片赋予一个新值
lst = [10, 20, 30, 40]
lst[2] = 100
print(lst)
lst[1: 3:] = [300, 400, 500, 600]
print(lst)





