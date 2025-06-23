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




class FileHandler:
    def __del__(self):  # Python 析构函数
        print("释放资源")

f = FileHandler()
del f  # 触发 __del__






class JustCounter:
    __secretCount = 0  # 私有变量（双下划线开头）
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1  # 可以访问私有变量
        self.publicCount += 1
        print (self.__secretCount)
 
counter = JustCounter()
counter.count()  # 输出 1
counter.count()  # 输出 2
print (counter.publicCount)  # 输出 2
#print (counter.__secretCount)  # 报错，实例不能访问私有变量

class Parent:                        # 定义父类
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):                 # 定义子类（继承Parent）
    def myMethod(self):
        print('调用子类方法')

c = Child()                          # 创建子类实例
c.myMethod()                         # 输出: 调用子类方法