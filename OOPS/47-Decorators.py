# Function Template
def funcReturner(num):
    """ Return Function """
    if num == 0:
        return print
    elif num==1:
        return int
    else:
        pass
A = funcReturner(1)
print(A) # <class 'int'>

def funcexecuter(func):
    """Passing the function as Argument"""
    func("This is a print statement")
funcexecuter(print)

def Decorator(func):
    def execution():
        print("Executing")
        func()
        print("Executed")
    return execution

# Method 1
def greeted():
    print("I Love learn....")
Var = Decorator(greeted)
Var()
# Method 2
@Decorator
def greet():
    print("I Love Python ....")
greet()