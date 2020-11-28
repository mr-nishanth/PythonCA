
def Factoial(NUMBER):
    """
    This is function is used to find the Factorial of Number's using For-Loops
    """
    factNum = 1
    for i in range(1, NUMBER+1):
        factNum *= i
    print(f"The Factoral of {NUMBER} is {factNum}")
Factoial(5)
print(Factoial.__doc__)