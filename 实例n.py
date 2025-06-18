def outer():
    # 外层函数的局部变量
    n = 10
    
    def inner():
        # 内层函数使用外层函数的局部变量
        print(n)
    
    # 外层函数的返回值是内层函数的函数名
    return inner


ot = outer()
ot()  # 输出: 10