# Python中的选择结构
 > 程序根据判断条件的布尔值选择性地执行部分代码
 明确的让计算机知道在什么条件下，该去做什么

## 单分支结构

```Python
print('-----以下模拟取款过程-----')
money = 1000  # 余额
out_take = int(input('请输入取款金额'))
# 判断余额是否充足
if money >= out_take:
    money = money - out_take
    print('取款成功，余额为：', money)
```

## 双分支结构
 **如果······不满足······就······**

```Python
print('从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数')
num = int(input('请输入一个整数'))
if num % 2 == 0:
    print(num, '\b是偶数')
else:
    print(num, '\b是奇数')
```

## 多分支结构

```Python
print('从键盘录入一个整数，判断成绩范围')
score_level = '''
成绩分布：
100-90  A
89-80   B
79-70   C
69-60   D
60-0    E
小于0或大于100为非法数据（不是成绩的有效范围
'''
print(score_level)
score = int(input('请输入一个成绩'))
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
elif 0 <= score <= 59:
    print('E')
else:
    print('错误！不是合法成绩值！')
```

## 嵌套if

```Python
a = '''
会员：
    >=200 8折
    >=100 9折
    <100  不打折
非会员：
    >=200 9.5折
    <200  不打折
'''
print(a)
vip_check = input('您是会员吗？y/n\n')
money = float(input('输入您的购物金额'))
if vip_check == 'y':
    if money >= 200:
        print('打8折，应付金额为：', money * 0.8)
    elif money >= 100:
        print('打95折，应付金额为：', money * 0.9)
    else:
        print('不打折，付款金额为：', money)
else:
    if money >= 200:
        print('打95折，应付金额为：', money * 0.95)
    else:
        print('不打折，付款金额为：', money)
```

## 条件表达式

```Python
print('从键盘录入两个数，比较两个整数的大小')
num_1 = int(input('请输入第一个整数'))
num_2 = int(input('请输入第二个整数'))
if num_1 >= num_2:
    print(num_1, '大于等于', num_2)
else:
    print((num_1, '小于', num_2))
print('-----如果使用条件表达式-----')
print((str(num_1) + '大于等于' + str(num_2)) if num_1 >= num2 else (str(num_1) + '小于' + str(num_2)))
```
