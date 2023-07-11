# print()函数的用法
可以输出数字
```Python
print(520)
print(98.5)
```
可以输出字符串
```Python
print('helloworld')
```

输出含有运算符的表达式
```Python
print(3+1)
print('3+1')
```
>3和1叫做操作数，加号叫做运算符，含有运算符和操作数的叫做表达式

将数据输出到文件中
```Python
fp=open('D:/test.txt','a+') # a+ 如果文件不存在就创建，存在就在文件的内容的后面继续追加
print('helloworld',file=fp)
fp.close()
```
**注意点：**
**1. 所指定的盘符要存在。**
**2.  使用file= fp。**

不进行换行输出（输出内容在一行当中）
```Python
print('hello','world','python')
```
