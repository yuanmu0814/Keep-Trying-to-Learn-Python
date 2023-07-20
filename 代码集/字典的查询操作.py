# 使用Python语言编写
# 创建时间 2023/7/17 18:54

# 字典的常用操作
# 字典中元素的获取
#   - []: scores['张三']
#   - get()方法： scores.get('张三')

print('-----第一种方式：使用[]-----')
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores['张三'])
print('-----第二种方式：使用gets()-----')
print(scores.get('张三'))
print(scores.get('陈六'))
print(scores.get('麻七', 99))


# []取值与使用get()取值的区别
#   - []如果字典中不存在指定的key，抛出KeyError异常
#   - gte()方法取值，如果字典中不存在指定的key，并不会抛出KeyError，而是返回None，可以通过参数设置默认的value，以便指定的key不存在时返回
