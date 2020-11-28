class Employee():
    workingHours=12
    pass

Sandy = Employee()
Sandy.name="VaseeKaran"
Sandy.salary=1000
Sandy.degree="IT"
Nandy=Employee()
Nandy.name="VijaySurya"
Nandy.salary = 2000
Nandy.degree = "B-Tech"
Nandy.workingHours=20

print(Sandy.name)
print(Sandy.salary)
print(Nandy.name)
print(Nandy.salary)

print(f" It's is Class Variable : {Employee.__dict__}")
print(Sandy.__dict__)
print(Nandy.__dict__)
A = Nandy.__dict__
print("Dict Format ", A)

Employee.workingHours = 24
print(f" It's is Class Variable : {Employee.__dict__}")