try:
    Num1 = input("Enter the number : ")
    Num2 = input("Enter the number : ")
    print(f"Sum of {int(Num1) * int(Num2)}")
except Exception as e:
    print(e)
    print("Enter the Numeric Values only ")

Num3 = input("Enter the number : ")
Num4 = input("Enter the number : ")
try:
    print(f"Sum of {int(Num3) + int(Num4)}")
except:
    print("This is a very important line.. ")