# 使用Python语言编写
# 创建时间 2023/7/15 14:42
#
# 嵌套循环
# 在循环结构中又嵌套了另外的完整的循环结构，其中内层循环作为外层循环的循环体执行
#
print('输出三行四列矩形')
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')  # 不换行输出
    print()  # 换行
print('-----------')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, end='\t')
    print()

# 二重循环中的break和continue
# 二重循环中的break和continue用于控制本层循环
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            break
        print(j)
print('-----------')
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            continue
        print(j, end='\t')
    print()
