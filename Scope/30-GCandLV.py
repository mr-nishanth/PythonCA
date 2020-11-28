print("With variables in function ")
a = 100
def fun1():
    a = 99
    print(a)
print("=================Local variables====================")
fun1()
print("=================Global variables===================")
print(a)

print("=========X===============X============X=========")
#------------------------------------------------------------------------------------------------------------>
print("Without variables in function ")
B = 55
def fun2():
    print(B)
print("=================Global variables for Access only ====================")
fun2()
print("=================Global variables===================")
print(B)
print("=========X===============X============X=========")
#------------------------------------------------------------------------------------------------------------>
C = 500
def fun3():
    c = 161
    print(C)
print("=================Global variables for Access only ====================")
fun2()
print("========= Local variables usage in side the Function =========")
#print(c)  # NameError: name 'c' is not defined
print("=========X===============X============X=========")#------------------------------------------------------------------------------------------------------------>
D = 555
def fun4():
    D += 45
    print(D)
print("=================Global variables====================")
print(D)
print("==== Can't Change Global variables (without using global Keywords) ====")
#fun4() # UnboundLocalError: local variable 'D' referenced before assignment
print("=========X===============X============X=========")
#------------------------------------------------------------------------------------------------------------>
N = 161
def fun5():
    global N
    N = 999
    print(N)
print("=========== Before Changing -->Global variables===========")
print(N)
print("==== Can Change Global variables (with using global Keywords) ====")
fun5()
print("============== After Changing -->Global variables==========")
print(N)
print("=========X===============X============X=========")
#------------------------------------------------------------------------------------------------------------>
M = 10
def fun6():
    global P
    P = 333
    print(P)
    return P
print("=========== Before Call Function ===========")
#print(P) # NameError: name 'P' is not defined
print("NameError: name 'P' is not defined")
print("=========== Global variables===========")
print(M)
print("==== After Call Function ====")
fun6()
print(f" New Global Variable is Created : {fun6()}")
print("=========X===============X============X=========")
#------------------------------------------------------------------------------------------------------------>
