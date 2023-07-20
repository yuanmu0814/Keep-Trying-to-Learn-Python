# 使用Python语言编写
# 创建时间 2023/7/17 18:54

# 字典的常用操作
# **key的判断**
#   - in：指定的key在字典中存在返回True
#   - not in：指定的key在字典中不存在返回True

scores = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in scores)
print('张三' not in scores)

# **字典键值对的删除**
print(scores)
del scores['张三']
print(scores)

# **字典元素的清空**
scores.clear()
print(scores)

# **字典元素的新增**
scores = {'张三': 100, '李四': 98, '王五': 45}
scores['陈六'] = 98
print(scores)

# **字典元素的修改**
scores['张三'] = 99
print(scores)


