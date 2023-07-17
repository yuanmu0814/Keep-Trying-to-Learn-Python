# 列表的查询操作
   ## 获取列表中指定的元素的索引
   **index()**
如查列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
```Python
lst_1 = ['hello', 'world', 98, 'hello']
print(lst_1.index('hello'))
```

如果查询的元素在列表中不存在，则会输出ValueError

```Python
lst_2 = ['hello', 'world', 98, 'hello']
print(lst_2.index('Python'))
```

还可以在指定的start和stop之间进行查找

```Python
lst_3 = ['hello', 'world', 98, 'hello']
print(lst_3.index('hello', 0, 3))
```

## 获取列表中的单个元素
   **获取单个元素**

```Python
lst_4 = ['hello', 'world', 98, 'hello', 'world', 234]
print(lst_4[2])   # 获取索引为2的元素
print(lst_4[-3])   # 获取索引为-3的元素
```
> Notes：
> - 正向索引从0到N-1
> - 逆向索引从-N到-1
> - 指定索引不存，抛出IndexError

 ## 获取列表中的多个元素
   **语法格式：`列表名[start: stop: step]`**
   - 列表的结果
     - 原列表片段的拷贝
   - 切片的范围
     - [start, stop)
   - step默认为1
     - 简写为[start: stop]，但实际范围为如前条所示
   - step为正数，从start开始往后计算切片
     - [: stop: step]
          - 切片后的第一个元素默认是列表的第一个元素
     - [start:: step]
          - 切片的最后一个元素默认是列表的最后一个元素
   - step为负数，从start开始往前计算切片
     - [: stop: step]
          - 切片的第一个元素默认是列表的最后一个元素
     - [start:: step]
          - 切片的最后一个元素默认是列表的第一个元素

```Python
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst[1: 6: 1])
print('原列表', id(lst))
lst_2 = lst[1: 6: 1]
print('切的列表', id(lst_2))
print(lst[1: 6])
print(lst[1: 6:])
print(lst[1: 6: 2])
print(lst[: 6: 2])
print('-----步长为负数的情况-----')
print(lst[::])
print(lst[:: -1])
print(lst[7:: -1])
print(lst[6: 0: -2])
```

 ## 判断指定的元素在列表中是否存在
**使用in和not in函数**
```Python
print('p' in 'python')
print('k' not in 'python')
lst = [10, 20, 30, 'python', 'hello']
print(10 in lst)
print(100 in lst)
print(100 not in lst)
```

## 列表元素的遍历
**使用for-in循环**
```Python
print('-----------')
lst = [10, 20, 30, 40]
for item in lst:
    print(item, end=' ')
```
