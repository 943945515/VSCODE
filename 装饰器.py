# def send():
#     print("发送消息")
# def send2():
#     print("发送消息2")

# def outer(fn):  # 装饰器函数
#     def inner():  # 包装函数
#         print("登录...")  # 新增功能
#         fn()  # 执行原函数
#         print("操作完成")  # 新增功能
#     return inner

# print("=== 方式1 ===")  # 手动应用装饰器方式1
# decorated_send = outer(send)  # 相当于 @outer
# decorated_send()  # 调用被装饰后的函数

# print("\n=== 方式2 ===")    # 手动应用装饰器方式2
# ot = outer(send2)
# ot()

# print("\n=== 方式3 ===")    # 使用@语法糖方式3
# @outer
# def send3():
#     print("发送消息3")
# send3() 

# def wrapper(func):
#     def inner(*args,**kwargs):
#         #执行被装饰函数之前的操作
#         ret = func(*args, **kwargs)
#         #执行被装饰函数之后的操作
#         return ret
#     return inner



# def outer(fn):        #定义外函数，它接受一个参数fn，fn将是一个函数对象
#     def inner():      #定义一个嵌套内函数inner
#         print("登录...")
#         fn()          #调用传入的函数fn（即被装饰的函数）
#     return inner      #返回内部定义的inner函数。
# #注意：装饰器名称后面不要加上(),前者是引用,后者是调用函数，返回该函数要返回的值
# @outer                #语法糖：下面的函数将被outer装饰，相当于outer(send)
# def send():           #定义了一个名为send的函数
#     print("发送消息:笑死我了")

# send()#调用send函数。但由于send被outer装饰，实际调用的是outer(send)返回的inner函数 '''




# def outer(fn):      # 定义装饰器函数outer，接收一个函数fn作为参数
#     def inner(name):# 定义内层函数inner，接收name参数
#         print(f"{name}是inner函数中的参数") # 打印传入的name参数
#         fn(name)    # 调用原始函数fn，并传入name参数
#     return inner    # 返回inner函数对象

# @outer                  # 使用装饰器语法，等价于 func = outer(func)
# def func(name):                # 定义被装饰的函数func，接收name参数
#     print("这是被装饰的函数")               # 打印"这是被装饰的函数"

# func('bingbing')    # 调用被装饰后的func函数，传入'bingbing'作为参数




def deco1(fn):  # 定义第一个装饰器deco1
    def inner():
        return "哈哈哈" + fn() + "呵呵呵"  # 在fn()返回值前后添加字符串
    return inner

def deco2(fn):  # 定义第二个装饰器deco2
    def inner():
        return "奈斯" + fn() + "非常优秀"  # 在fn()返回值前后添加字符串
    return inner

@deco1  # 先应用deco2，再应用deco1（装饰器从下往上执行）
@deco2  # 第一个应用的装饰器
def test1():
    return "晚上在学习python基础"  # 原始函数返回值

print(test1())  # 调用被双重装饰后的函数