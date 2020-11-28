# 0 1 1 2 3 5 8 13 21
# A+B=C | | |
#   A+B=C | |
#     A+B=C |
#       A+B=C
# Logic A=B and B=C
print("Fibonacci Series")
def fibo(x):
    """ Print the Fibonacci Series """
    if x == 1:
        print(0)
    elif x <= 0:
        print("No Negitive Series")
    else:
        A = 0
        B = 1
        print(A)
        print(B)
        for i in range(2, x):
            C = A + B
            A = B
            B = C
            print(C)
fibo(2)
