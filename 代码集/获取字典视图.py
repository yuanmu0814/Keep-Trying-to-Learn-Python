# 使用Python语言编写
# 创建时间 2023/7/17 18:54

# 获取字典视图的三个方法
#   - keys()：获取字典中所有key
#   - values()：获取字典中所有value
#   - items()：获取字典中所有key-value对

scores = {'张三': 100, '李四': 98, '王五': 45}
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有key组成的视图转成列表
values = scores.values()
print(values)
print(type(values))
print(list(values))
items = scores.items()
print(items)
print(list(items))  # 转换后的列表元素是由元组组成的

