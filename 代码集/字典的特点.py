# 使用Python语言编写
# 创建时间 2023/7/20 21:04

# 字典的特点：
#   - 字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
#   - 字典中的元素是无序的
#   - 字典中的key必须是不可变对象
#   - 字典也可以根据需要动态地伸缩
#   - 字典会浪费较大的内存，是一种使用空间换时间的数据结构

scores = {'name': '张三', 'name': '李四'}
print(scores)  # 输出`{'name': '李四'}`，key不允许重复
scores = {'name': '张三', 'nickname': '张三'}
print(scores)  # 输出`{'name': '张三', 'nickname': '张三'}`,value可以重复

lst = [10, 20, 30]
lst.insert(1, 100)
print(lst)
