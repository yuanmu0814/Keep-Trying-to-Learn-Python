# Python中的元祖
 元祖是Python内置的数据结构之一，是一个不可变序列
 > 不可变序列与可变序列：
 >  - 不可变序列：如字符串、元组。没有增、删、改的操作
 >  - 可变序列：如列表、字典。可以对序列执行增、删、改操作，对象地址不发生改变

```Python
lst = [10, 20, 30]
print(id(lst))
lst.append(300)
print(id(lst))

s = 'hello'
print(id(s))
s = s + 'world'
print(s)
print(id(s))
```

 为什么要将元组设计成不可变序列
   - 在多任务环境下，同时操作对象时不需要加锁
   - 因此，在程序中尽量使用不可变序列

 注意事项：元组中储存的是对象的引用
   - 如果元组中对象本身不可变对象
   - 如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变

```Python
t = (10, [20, 30], 9)
print(t)
print(type(t))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))
print('-----尝试将t[1]修改为100-----')
# t[1] = 100
# TypeError: 'tuple' object does not support item assignment
print('由于[20， 30]是列表，而列表是可变序列，所以可以向列表中添加元素，而列表的内存地址不变')
t[1].append(100)
print(t, id(t[1]))
```
