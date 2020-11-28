# @property ==> it's used to change the property  [method or function] to [attribute]

class Employee:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname =lname
        #self.email = f"{fname}.{lname}@gmail.com" # ==> 1

    @property # 2
    def email(self):
        return f"{self.firstname}{self.lastname}@gmail.com"
    def explain(self):
        return f"This Employee name is {self.firstname} {self.lastname}"
csk = Employee("Cyber", "Nishanth")
print(csk.explain())
print(csk.email)
print("\n Changing the firstname ")
csk.firstname = "Hacker"
print(csk.email)
#print(csk.email) # ==> 1
#print(csk.email())
print("\n After addind @property ") # 2
print(csk.email)
csk.email="csk@gmail.com"
#print(csk.email) # AttributeError: can't set attribute  ( see 2 ) here email is method then we convert attribute but email is method so can't change the value


