# Default --> str()



a = 100
print(type(a), str(a) , type(a))
print(type(a), repr(a), type(a))
print("BackGround Process")
print(int.__str__(a))
print(a.__str__())
print(a.__repr__())
print("==================================")
a = 'Cyber'
print(type(a), str(a) , type(a))
print(type(a), repr(a), type(a))
print("BackGround Process")
print(int.__str__(a))
print(a.__str__())
print(a.__repr__())
print("==================================")
a = "Cyber"
print(type(a), str(a) , type(a))
print(type(a), repr(a), type(a))
print("==================================")

print("Operator Overloading in str() and repr() ")

class Employe():
    workingHours = 12
    #Constructors Start
    def __init__(self,aname,asalary,adegree):
        self.name = aname
        self.salary = asalary
        self.degree = adegree
    #Constructors End

    def printDetails(self,no):
        return f"my id {no} and my name is {self.name} , Salary is {self.salary} and the degree is {self.degree}"

    def __str__(self): # 1
            return f" my name is {self.name} , Salary is {self.salary} and the degree is {self.degree}"

    def __repr__(self):
        return f" I am From Repr Function"


Cyber = Employe("Nishanth", 1000, "Maths")
Love = Employe("Cyber", 3456, "Computer")
print(Love)  # Return <__main__.Employe object at 0x00000237F7474F70>
print("BackGround Process ")
print(Love.__str__())
print(" adding __str__ method \n ") # 1
print(Cyber)
print(" adding __repr__ method \n ")
print(repr(Cyber))