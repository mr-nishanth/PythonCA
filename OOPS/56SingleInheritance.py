class Employe():
    workingHours = 12
    def __init__(self,aname,asalary,adegree):
        """ Constructors """
        self.name = aname
        self.salary = asalary
        self.degree = adegree
    @classmethod
    def splitter(cls, Alt_Construct):
        """ Here The String was split by ( - ) and store in Splitted """
        return cls(*Alt_Construct.split("-"))
    def printDetails(self):
        return f"This is {self.name} , my salary is {self.salary} and my degree is {self.degree}"
class Programmer(Employe):
    print("I am from Programmer Class")
    def __init__(self, pname, psalary, pdegree, planguage):
        self.name = pname
        self.salary = psalary
        self.degree = pdegree
        self.language = planguage
    def printProg(self):
        return f"This is {self.name} , my salary is {self.salary} and my degree is {self.degree}... I Love {self.language} language "

Nisha = Programmer.splitter("Vijay-4567-Tamil-Python")
print(Nisha.__dict__)
print(Nisha.printProg())
print(Nisha.printDetails())