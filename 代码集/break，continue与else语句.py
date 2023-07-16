# 使用Python语言编写
# 创建时间 2023/7/15 14:42

# 流程控制语句break
# break语句
# 用于结束循环结构，通常与分支结构if一起使用
print('从键盘录入密码，最多录入三次，如果正确就结束循环')
for item in range(3):
    pwd = input('请输入密码\n')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
a = 0
while a < 3:
    pwd = input('请输入密码\n')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a += 1

# 流程控制语句continue
# 用于结束当前循环，进入下一次循环，通常与分支结构中的if一起使用
print('要求输出1~50所有5的倍数')
for item in range(1, 51):
    if item % 5 == 0:
        print(item)

print('-----如果要求使用continue-----')
for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)

# else语句
# 与else语句搭配使用的三种情况
#   - if-else：if条件表达式不成立时执行else
#   - while-else：没有遇到break时执行else
#   - for-else：没有遇到break时执行else
for item in range(3):
    pwd = input('请输入密码\n')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起，您已经三次输入错误')

a = 0
while a < 3:
    pwd = input('请输入密码')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a += 1
else:
    print('对不起，您已经三次输入错误')
