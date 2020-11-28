from functools import reduce
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 0
print("==== Normal Method ====")
for i in List:
    num += i
print(num)
#<=====================================================================================>
print("====  Reduce Function ====")
#Cumulative left to right
"""
Reduce Function Working
(((((x+y)+y)+y)+y)+y)

"""
Reduce = reduce(lambda x, y: x + y, List)
print(Reduce)
List1=[1,2,3,4,5] # 120
RReduce = reduce(lambda x, y: x * y, List)
print(RReduce)
