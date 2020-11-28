for i in range(1, 101):
    pass

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even = list(filter(lambda a: a % 2 is  0, List))
print("Even Numbers ")
print(Even, " ==> ", type(Even))

Odd = list(filter(lambda a: a % 2 is not 0, List))
print("Odd Numbers ")
print(Odd, " ==> ", type(Odd))
