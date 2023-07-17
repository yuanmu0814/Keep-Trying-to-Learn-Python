# 使用Python语言编写
# 创建时间 2023/7/16 16:42

# 列表元素的排序操作
# 常用的两种方式：
#   - 调用sort()方法，列表中所有的元素默认按照从小到大的顺序进行排序，可以指定reverse=True，进行降序操作
#   - 调用内置函数sorted()，可以指定reverse = True，进行降序操作，原列表不发生改变
lst = [20, 40, 10, 98, 54]
print('排序前：', lst, id(lst))
lst.sort()
print('排序后：', lst, id(lst))
lst.sort(reverse=True)
print('降序排序后：', lst, id(lst))
print('----------')
print('使用内置函数sorted()对列表进行排序，将产生一个新的列表对象')
lst = [20, 40, 10, 98, 54]
print('原列表：', lst)
new_lst = sorted(lst)
print(lst)
print(new_lst)
new_lst = sorted(lst, reverse=True)
print(new_lst)




