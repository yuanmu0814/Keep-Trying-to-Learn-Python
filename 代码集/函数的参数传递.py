# 函数的参数传递
# 函数调用的参数传递
#   - 位置实参
#       - 根据形参对应的位置进行实参传递
#   - 关键字实参
#       - 根据形参名称进行实参传递
def calc(a, b):  # a，b称为形式参数，简称形参，形参的位置是在函数的定义处
    c = a + b
    return c
result = calc(10, 20)  # 10，20称为实际参数的值，简称实参，实参的位置是函数的调用处
print(result)

result = calc(b = 10, a = 20)  # =左侧的变量的名称称为关键字参数
print(result)

def fun(arg1, arg2):
    print('arg1=', arg1)
    print('arg2=', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1=', arg1)
    print('arg2=', arg2)

n1 = 11
n2 = [22, 33, 44]
print(n1)
print(n2)
print('----------')
fun(n1, n2)  # 将位置传参，arg1，arg2是函数定义处的形参，n1，n2是函数调用处的实参。
# 总结：实参名称与形参名称可以不一致
print(n1)
print(n2)

# 在函数调用过程中，进行参数的传递
# 如果是不可变对象，在函数体的修改不会影响实参的值 
# arg1的值修改为100，不会影响n1的值
# 如果是可变对象，在函数体内的修改会影响到实参的值 
# arg2的修改，append(10)，会影响到n2的值
