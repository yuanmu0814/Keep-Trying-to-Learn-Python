# 使用Python语言编写
# 创建时间 2023/7/21 16:51

# 集合的相关操作
# 集合元素的判断操作
#   - in或not in
# 集合元素的新增操作
#   - 调用add()方法，一次添中一个元素
#   - 调用update()方法至少添中一个元素
# 集合元素的删除操作
#   - 调用remove()方法，一次删除一个指定元素，如果指定的元素不存在抛出KeyError
#   - 调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不抛异常
#   - 调用pop()方法，一次只删除一个任意元素
#   - 调用clear()方法，清空集合

print('''集合元素的判断操作''')
s = {10, 20, 30, 40, 50, 60}
print(10 in s)
print(100 not in s)
print('''集合元素的新增操作''')
s.add(70)
print(s)
s.update({200, 300, 400})  # 一次至少添加一个元素
print(s)
s.update([100, 99, 8])
s.update((78, 79, 80))
print(s)

print('''集合元素的删除操作''')
s.remove(100)
print(s)
s.discard(500)
print(s)
s.pop()  # 不难填写参数
print(s)
s.pop()
print(s)
s.clear()
print(s)
