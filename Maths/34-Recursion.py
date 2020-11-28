# What is the Limit of Recursion ?
#import sys
#sys.setrecursionlimit(100)
def factNum(num):
    """ This is function is used to find the Factorial of Number's using Recursion """
    if num == 0:
        return 1
    return num * factNum(num - 1)
print(factNum(5))
