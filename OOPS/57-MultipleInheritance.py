class Employe():
    Var=1
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
    @staticmethod
    def staticMethod(pas):
        print("I Like my {pas}")

class Player:
    Var=2
    no_of_game = 4
    def __init__(self,name="name missing",game="Pass the game"):
        self.name = name
        self.game= game
Africe=Player("Bolt","VolleyBAll")
print(Africe.name)

class CoolProgrammer( Employe,Player):
    Var=3
    pass
Elite = CoolProgrammer.splitter("Hate-1232-Space")
print(Elite.__dict__)
print(Elite.no_of_game)
print(Elite.printDetails())
print(Elite.Var)