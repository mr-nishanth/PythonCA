class Employe():
    workingHours = 12
    def __init__(self,aname,asalary,adegree):#Constructors Start
        self.name = aname
        self.salary = asalary
        self.degree = adegree
    #Constructors End


    def printDetails(self):
        return f"my id {no} and my name is {self.name} , Salary is {self.salary} and the degree is {self.degree}"

    # Class method here cls is like self ,self denote the object and cls is denote the object class
    # cls vanthu object yoda class ah argument ah pakuim

    @classmethod
    def changeWorkingHours(cls, new_CWH):  # Usage: Now we can change the class variable using of
        cls.workingHours = new_CWH

print(Employe.workingHours)
Cyber = Employe("Nishanth", 1000, "Maths")
Love = Employe("Cyber", 3456, "Computer")
print("Cyber ", Cyber.degree, " Love ", Love.salary)
#Cyber.changeWorkingHours(8)
print(Cyber.__dict__)
print(Love.__dict__)
Cyber.workingHours="5"
print(Cyber.__dict__)
print(Cyber.__dict__)
print(Employe.workingHours)