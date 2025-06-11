#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py
import math
import time

print('he');print('runoob');

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错
    print ("False")
input("按下 enter 键退出，其他任意键显示...\n")
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
x="a"
y="b"
#换行输出
print (x)
print (y)
print ('------')
#不换行输出
print(x,y)
A, B, C = 1, "赵九州", "john"
print(A, B, C)

list=['adfhsaj','jack','run']#列表
list.append('jia')#列表添加元素
del list[2]#删除列表元素
list[1]='zhao'
nextlist=['zjz']
print(list[1:]+nextlist)
letter=['a','d','e','z','p','g']
print(letter[0:4:2])#取0和3，步长为2

dict = {}                    #字典
dict['one'] = "This is jsjvhv"
dict[2] = "This is sg"
tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}
print (dict['one'])          # 输出键为'one' 的值
print (dict[2])              # 输出键为 2 的值
print (tinydict)             # 输出完整的字典
print (tinydict.keys())      # 输出所有键
print (tinydict.values())    # 输出所有值

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0
#下面都是二进制运算
c = a & b;  # 12 = 0000 1100 按位与
print("1c 的值为：", c)
c = a | b;  # 61 = 0011 1101 按位或
print("2c 的值为：", c)
c = a ^ b;  # 49 = 0011 0001 按位异或
print("3c 的值为：", c)
c = ~a;  # -61 = 1100 0011  按位取反
print("4c 的值为：", c)
c = a << 2;  # 240 = 1111 0000 左移位
print("5c 的值为：", c)
c = a >> 2;  # 15 = 0000 1111 右移位
print("6c 的值为：", c)

y= 4
u= 4
list = [ 3, 4, 5];
if (y in list):
    print("变量 y 在给定的列表中 list 中")
else:
    print("变量 y 不在给定的列表中 list 中")
if (y is not u):
    print("y和u没有相同标识")
else:
    print("y和u有相同标识")

count = 1
while (1):
    print('The count is:', count)
    count = count + 1
    if count > 3:  # 当i大于10时跳出循环
        break
print("Good bye!")
#for循环
for num in range(10,13):  # 迭代 10 到 20 (不包含) 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)

print(dir(math))
print ("My name is %s and weight is %d kg" % ('zjz', 55))

tinydict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
tinydict1['Age'] = 24  # 更新
tinydict1['School'] = "DONGRUAN"  # 添加
print("tinydict1['Age']: ", tinydict1['Age'])
print("tinydict1['School']: ", tinydict1['School'])

ticks = time.time()
print("当前时间戳为：",ticks)#获取当前时间戳
localtime = time.localtime(time.time())#获取当前时间
print("本地时间为:",localtime)
asctime = time.asctime(time.localtime(time.time()))
print("当前时间为",asctime)
# 格式化成像2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#自定义函数
def pr(str):
    "打印输入的字符串"
    print(str)
    return
#调用函数
pr("我正在调用自定义函数pr")

def cha(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return
# 调用cha函数
mylist = [10, 20, 30]
cha(mylist)
print("函数外取值: ", mylist)


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50,99)


# 全局变量和局部变量
total = 0  # 这是一个全局变量
def su(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total
# 调用su函数
su(10, 20)
print("函数外是全局变量 : ", total)

fo = open("foo.txt", "w")
fo.write("www.runoob.com!\nVery good site!\n")
# 关闭打开的文件
fo.close()
fo = open("foo.txt", "r+")
str = fo.read(10)#读取十个字符
print ("读取的字符串是 : ", str)
# 关闭打开的文件
fo.close()

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()

def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("参数没有包含数字\n",Argument)
temp_convert("xyz")

#创建一个类Person  self 代表的是类的实例，代表当前对象的地址，而 self.__class__ 则指向类。
class Person:
    def __init__(self, name, age): #初始化方法，创建新实例时自动调用
        self.name = name  # 实例属性
        self.age = age    # 实例属性
    def greet(self):
        print(f"Hello, I'm {self.name}, {self.age} years old.")
# 创建实例（自动调用 __init__）
p1 = Person("Alice", 25)
p1.greet()  # 输出: Hello, I'm Alice, 25 years old.


class Employee:
    '所有员工的基类'
    empCount = 0    #所有实例共享的一个类变量
    def __init__(self, name, salary):   #创建新实例时自动调用该构造函数
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()  #对象emp1调用类中创建的函数
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)#%d十进制整数占位符
'后面的 % 的作用是将Employee.empCount的值填充到 %d 的位置。'


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):  #使用print()/str()自动调用__str__
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self, other):   #执行+时，Python会自动调用__add__
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

import re
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span()) # 不在起始位置匹配

#测试一下更新后上传GitHub
#6月10日测试vscode修改后上传至GitHub
#6月11日测试vscode修改后上传至GitHub