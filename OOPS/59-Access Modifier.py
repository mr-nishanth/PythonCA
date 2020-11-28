# Access Modifier
# Access Specifier
'''
Public
Private  ==> __Variavle_name or __function_name --> Double Underscore
Protected  ==> _Variavle_name or _function_name --> Single Underscore
'''
class Employe():
    Var = 1
    __workingHours = 12
    _totalDays=31
    A = 1
    B = 2
    C = A + B
    def adder(self):
        return f"The sum is {self.C} "
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
    def printer(self):
        return self.__workingHours
    @staticmethod
    def staticMethod(pas):
        pass

class CoolProgrammer(Employe):
    pass

csk=Employe.splitter("CSK-59867-CRICKETER")
print(csk.__dict__)
print(csk.printDetails())
#print(csk.__workingHours) # 'Employe' object has no attribute '__workingHours'
print(csk.printer())
print(csk.adder())

rcb = CoolProgrammer.splitter("RCB-35252-SUMA")
# print(rcb.__workingHours)
print(rcb._totalDays)

#Using Name Mangling for access the private things
print(rcb._Employe__workingHours)