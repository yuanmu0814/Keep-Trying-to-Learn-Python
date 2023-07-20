# 使用Python语言编写
# 创建时间 2023/7/20 21:14

# 字典生成式
# 内置函数zip()
#   - 用于将可迭代的对象作为参数，将对象中的元素打包成一个元祖，然后返回由这些元祖组成的列表

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]

scores = {item: price for item, price in zip(items, prices)}
print(scores)
