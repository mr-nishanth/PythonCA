# Self Refer the Object or Denote the Object
# self vanthu object  ah argument ah pakuim
# class Employee():
#     workingHours = 12
#     def printDetails(self,no):
#         return f"my id {no} and my name is {self.name} , Salary is {self.salary} and the degree is {self.degree}"

# Sandy = Employe()
# Sandy.name="VaseeKaran"
# Sandy.salary=1000
# Sandy.degree="IT"
# Nandy=Employe()
# Nandy.name="VijaySurya"
# Nandy.salary = 2000
# Nandy.degree = "B-Tech"
# Nandy.workingHours=20
# print(Nandy.printDetails(99))
# print(Sandy.printDetails(55))

# <====================================  Constructors ==========================================>
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

Cyber = Employe("Nishanth", 1000, "Maths")
Love = Employe("Cyber", 3456, "Computer")
print(Cyber.degree)
print(Love.salary)
print(Cyber.printDetails(55))
# <====================================  Constructors ==========================================>