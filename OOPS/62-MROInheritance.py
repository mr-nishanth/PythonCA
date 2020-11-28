# Method Resolution Order or Diamond Shape
# Python program to show the order
# in which methods are resolved
'''
class A:
    def rk(self):
        print(" In class A")
class B:
    def rk(self):
        print(" In class B")

# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")

r = C()

# it prints the lookup order
print(C.__mro__)
print(C.mro())

'''

class A:
    def zz(self):
        print("\n I am from class A")
        return "I am From class A"
class B(A):
    def zz(self):
        print("\n I am from class B")
        return "I am From class B"
class C(A):
    def zz(self):
        print("\n I am from class C")
        return "I am From class C"
class D(B,C):
    def zz(self):
        print("\n I am from class D")
        return "I am From class D"

a = A()
b = B()
c= C()
d= D()

print(d.zz())