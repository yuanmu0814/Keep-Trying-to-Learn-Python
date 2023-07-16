# 使用Python语言编写
# 创建时间 2023/7/15 14:41

# 循环结构
# - 重复做同一件事的情况，称为循环
# - 循环的分类
#   - while
#   - for-in

# while循环
# - 选择结构的if与循环结构while的区别
#   - if是判断一次，条件为True执行一次
#   - while是判断N+1次，条件为True执行N次

a = 1
# 判断条件表达式
if a < 10:
    print(a)
    a += 1
while a < 10:
    print(a)
    a += 1

# while循环的执行流程
# **四步循环法**
#   -初始化变量
#   -条件判断
#   -条件执行体（循环体）
#   -改变变量

a = 0
sum = 0
while a < 5:
    sum += a
    a += 1
print('和为', sum)

print('-----计算1~100之间的偶数和-----')
i = 1
sum = 0
while i <= 100:
    if i % 2 ==0:
        sum += i
    i += 1
print('和为', sum)
sum = 0
i = 1
while i <= 100:
    if not bool(i % 2):
        sum += i
    i += 1
print('和为', sum)

# for-in循环
# for-in循环：
#   - in表达从（字符串、序列等）中依次取值、又称为遍历
#   - for-in遍历的对象必须是可迭代对象
# **循环体内不需要访问自定义变量，可以将自定义变量替代为下划线**

for item in 'Python':
    print(item)
for i in range(10):
    print(i)
for _ in range(5):
    print('这句话将重复五次')
print('-----使用for-in循环计算1~100之间的偶数和-----')
sum = 0
for item in range(1, 101):  # 注意要取到100则右侧需要写为101
    if item % 2 == 0:
        sum += item
print('1~100之间的偶数和为：', sum)

print('-----输出100~999的水仙花数-----\n例如：\n153=3*3*3+5*5*5+1*1*1')
for item in range(100, 1000):
    ge = item % 10          # 个位
    shi = item // 10 % 10   # 十位
    bai = item // 100 % 10   # 百位
    if ge ** 3 + shi ** 3 + bai ** 3 == item:
        print('发现水仙花数：', item)

