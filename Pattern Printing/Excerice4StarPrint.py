starInput = int(input("How many row's of stars do you want ? : "))
print(starInput)
boolInput=bool(int(input("Enter the number [ Note : 1 for Forward or 0 for Backward ] : ")))
print(boolInput)
if boolInput == True:
    for i in range(1, starInput + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

else:
    for i in range(starInput, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print()