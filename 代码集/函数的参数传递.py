# 函数的参数传递
# 函数调用的参数传递
#   - 位置实参
#       - 根据新昌对应的位置进行实参传递
#   - 关键字实参
#       - 根据形参名称进行实参传递
def calc(a, b):  # a，b称为形式参数，简称形参，形参的位置是在函数的定义处
    c = a + b
    return c
result = calc(10, 20)  # 10，20称为实际参数的值，简称实参，实参的位置是函数的调用处
print(result)

result = calc(b = 10, a = 20)
print(result)
