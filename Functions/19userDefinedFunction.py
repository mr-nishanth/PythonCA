print("Learn Built-in or User Defined Function ")
a = 10
b = 15
print(f"Sum of {a} and {b} is {sum((a,b))} ")
print("==============================================")
def avgFun(a, b):
    """ This Function return's average using Print function """ # DocString
    avg = (a+b)/2
    print(avg)
avgFun(10,10)
A=avgFun(10,10)
print(A)
print(avgFun.__doc__)
print("==============================================")
def avg(a, b):
    """ This Function return's average using return keyword it's used to Store the values""" # DocString
    return (a+b)/2
avg(10,10)
R=avg(10,10)
print(R)
print(avg.__doc__)

def function():
    """ Learn Copy and Delete the Function """
    print("Cyber-Nishanth")
function()

Function=function # Like Copy
del function
Function()