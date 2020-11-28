# + , - , * , /
# On Google Searching Mapping Operators to Function
print(15 + 20)
print("Hello " + " World")

a = 5
b = 20
print(a+b)

#b = "Hello"
#print(a+b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(int.__add__(a,b))
print(int.__sub__(a,b))
print(int.__mul__(a,b))
print(int.__floordiv__(a, b))

print("======================================================")

class Employe():
    #Constructors Start
    def __init__(self,aname,asalary,adegree):
        self.name = aname
        self.salary = asalary
        self.degree = adegree
    #Constructors End

    def printDetails(self,no):
        return f"my id {no} and my name is {self.name} , Salary is {self.salary} and the degree is {self.degree}"
    def __add__(self, other):
        return self.salary + other.salary
    def __sub__(a,b):
            return a.salary - b.salary
    def __mul__(c, d):
        return "I will be Hacker"

Cyber = Employe("Nishanth", 5600, "Maths")
Love = Employe("Cyber", 3456, "Computer")

print(Cyber.salary + Love.salary)
print(Cyber+Love)
print(Cyber-Love)
print(Cyber*Love)