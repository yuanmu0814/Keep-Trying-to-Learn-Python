# 内置函数range()
 range()函数
 - 用于生成一个整数序列
 - 创建range对象的三种方式
   - range(stop)   创建一个(0,stop)之间的整数序列，步长为1
   - range(start, stop)    创建一个(start, stop)之间的整数序列，步长为1
   - range(start, stop, step)  创建一个(start, stop)之间的整数序列，步长为step
 - 返回值是一个迭代器对象
 - range类型的优点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，因为仅仅需要储存start，stop和step，只有当用到range对象时，才会去计算序列中的相关元素
 - in/not in 判断整数序列中是否存在/不存在指定的整数

```Python
r = range(10)
print(r)
print(list(r))  # list()此处用于查看range对象中的整数序列

r = range(1, 10)
print(list(r))

r = range(1, 10, 2)
print(list(r))

print('-----判断指定的整数在序列中是否存在：in，not in-----')
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)
```
