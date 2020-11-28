Numbers = ["33", "44", "11", "22", "55"]
Number=len(Numbers)
print(f"Length of number : {Number}")
print(Numbers, " ==> ", type(Numbers))
for i in range(len(Numbers)):
    print(Numbers[i], " ==> ", type(Numbers[i]))
    Numbers[i] = int(Numbers[i])
    print(Numbers[i], " ==> ", type(Numbers[i]))

#<=====================================================================================>
Numbers = ["33", "44", "11", "22", "55"]
print("====> Before Map function <====")
print(Numbers, " ==> ", type(Numbers))
print(Numbers[0], " ==> ", type(Numbers[0]))
#<=====================================================================================>

print("====> After Map function <====")
Map = list(map(int, Numbers))
print(Map, " ==> ", type(Map))# Returns Object
print(*Map, " ==> ", type(Map))
print(Map[0], " ==> ", type(Map[0]))
#<=====================================================================================>

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Sqr = list(map(lambda a: a * a, List))
print(Sqr)
#<=====================================================================================>