class Employe():
    workingHours = 12
    #Constructors Start
    def __init__(self,aname,asalary,adegree):
        """ Constructors """
        self.name = aname
        self.salary = asalary
        self.degree = adegree
    #Constructors End
    @classmethod
    def splitter(cls, Alt_Construct):
        """ Here The String was split by ( - ) and store in Splitted """
        # Splitted = Alt_Construct.split("-")
        # return cls(Splitted[0], Splitted[1], Splitted[2])
        # or |
        return cls(*Alt_Construct.split("-"))
Cyber = Employe.splitter("Nishanth-1000-Maths")
print(Cyber.__dict__)
Love = Employe.splitter("Cyber-3456-Computer")
print(Love.__dict__)
Soccer = Employe.splitter("CSK-99999-Cricket")
print(Soccer.__dict__)