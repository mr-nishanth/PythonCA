# Instance and Object are same
class Student():
    pass

Nisha = Student()
Nisha.name = "Nishanth" # Here name is a instance variable for Nisha( instance or Object) from Student Class
Nisha.age = 20
Nisha.city="Sathy"

Cyber = Student()
Cyber.name = "Cyber-Nishanth" # Here name is a instance variable for Cyber ( instance or Object) from Student Class
Cyber.age = 25
Cyber.city = "Erode"

print(Nisha.city)
print(Cyber.name)