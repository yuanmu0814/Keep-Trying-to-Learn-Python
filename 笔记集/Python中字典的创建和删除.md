# Python中字典的创建和删除
## 字典的创建
   - 最常用的方式：使用花括号
   - 使用内置函数dict()
```Python
print('-----使用[]创建字典-----')
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores)
print(type(scores))
print('-----使用dict()-----')
student = dict(name='jack', age='20')
print(student)
print('-----空字典-----')
d = {}
print(d)
```

## 删除字典
```Python
del scores
```
