# First Prefrence instance Variable then Class Variable
'''
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside the constructor of Class A"
        self.classvar1 = "I am inside the constructor of Class A"
class B(A):
    classvar2 = "I am a class variable in class B"


a = A()
b = B()

print(b.classvar1)
print(b.var1)
print(b.classvar1)
print(b.classvar2)
'''

'''
print("=======> OverRiding Constructor <=======")
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside the constructor of Class A"
        self.classvar1 = "I am inside the constructor of Class A"
        self.special="Special"
class B(A):
    #classvar1 = "I am a class variable in class B" # -->2
    def __init__(self):
        self.var1 = "I am inside the constructor of Class B"
        #self.classvar1 = "I am inside the constructor of Class B" # -->1

a = A()
b = B()

print(b.classvar1)
print("\n After Commeting the B classvar1 Constructor")
print(b.classvar1)
print("\n After Commeting the  B classvar1 Class_Variable")
print(b.classvar1)
'''

print("\n Now we see How to access the base class Constructor from derived class with own Constructor")
# Using Super fun
# Syntax
# [super().] ==> Super Class la or Base class la irrukara [__init__()] Constructor ah run pannu
# super().__init__() --> like Copy ==>{Super Class Constructor copy and paste in Derived class }

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside the constructor of Class A"
        self.classvar1 = "I am inside the constructor of Class A"
        self.special="Special"
class B(A):
    #classvar1 = "I am a class variable in class B" # -->2
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside the constructor of Class B"
        self.classvar1 = "I am inside the constructor of Class B" # -->1

a = A()
b = B()

print(b.special)
print("After Comment-out the B class Constructor ")
print(b.classvar1)