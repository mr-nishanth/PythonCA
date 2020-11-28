#

Var1 = 56
Var = int(input("Enter the values : "))
if Var > Var1:
    print(f"{Var} is Greater then {Var1} ")
elif Var == Var1:
    print(f"{Var} is Equal to  {Var1} ")
else:
    print(f"{Var} is Smaller then {Var1} ")

age = int(input('Enter your age : '))
if age < 1:
    print("Enter Valid Age..")
elif age > 18:
    print("You can drive..")
elif age == 18:
    print("We will think..")
else:
    print("You Can't Drive")