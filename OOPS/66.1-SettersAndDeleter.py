# Setter --> Syntax
# @method_name.setter
class Employee:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname =lname
        #self.email = f"{fname}.{lname}@gmail.com" # ==> 1
    @property # 2
    def email(self):
        if self.firstname == None or self.lastname == None:  # ==> 5
            return "Email is not set"
        return f"{self.firstname}{self.lastname}@gmail.com"
    @email.setter
    def email(self, string):
        names = string.split("@")[0]  # [csk.007,gmail.com]
        # names=names[0] or string.split("@")[0] both are same
        self.firstname=names.split(".")[0]  # [csk,007]
        self.lastname = names.split(".")[1]
    @email.deleter # 4
    def email(self):
        self.firstname = None
        self.lastname =None

    def explain(self):
        return f"This Employee name is {self.firstname} {self.lastname}"
csk = Employee("Cyber", "Nishanth")
print(csk.email)
csk.firstname = "hacker"
print(csk.email)
csk.email = "csk.007@gmail.com"
print(csk.email)

# del csk.email # AttributeError: can't delete attribute ( see 4 up )
print("\n After delete the csk")
del csk.email
print("\n After delete the csk and print ")
print(csk.email) # NoneNone@gmail.com (see 5 up)
