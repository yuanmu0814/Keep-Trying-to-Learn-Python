# 使用Python语言编写
# 创建时间 2023/7/16 16:41

# 为什么需要列表？
# - 变量可以存储一个元素，而列表是一个“大容器”可以储存N多个元素，程序可以方便地对这些数据进行整体操作
# - 列表相当于其他语言中的数组/结构体
a = 10
lst = ['hello', 'world', 98]
print(id(lst))
print(type(lst))
print(lst)

# 列表的创建
# 列表需要使用中括号[]，元素之间使用英文的逗号进行分隔
# 列表的创建方式
#   - 使用中括号
#   - 调用内置函数list()
lst = ['hello', 'world', 98]
lst2 = list(['hello', 'world', 98])

# 列表的特点
#   - 列表元素按顺序有序排序
#   - 索引映射唯一个数据
#   - 列表可以存储重复数据
#   - 任意数据类型混存
#   - 根据需要动态分配和回收内存
lst = ['hello', 'world', 98]
print(lst[0], lst[-3])




