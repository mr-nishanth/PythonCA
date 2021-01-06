# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 19:53:53 2020

@author: Nishanth
"""

print("Normal Method")
List_3rd_table=[]
for i in range(3,33,3):
    List_3rd_table.append(i)
print(List_3rd_table)

#================================================

print("Comprehensions")
List_1 = [ i for i in range(3,33,3) ]
print( List_1 )


List_2 = [ i for i in range(1,31) if i%3==0 ]
print( List_2 )

#================================================

print("Dict Comprehensions")
Normal_Dict={0:"item0",1:"item1",2:"item2"}

Comprehensions_Dict = {i:f"item{i}" for i in range(1,11)}
print(Comprehensions_Dict)

print("Reverse the Dict")

Re_Dict= { value:key for key,value in Comprehensions_Dict.items()}
print(Re_Dict)

#================================================

print("Generator Comprehensions")
evens=( i for i in  range(1,11) if i%2==0)
print(type(evens))

print(evens.__next__())
print(next(evens))
print(evens.__next__())
print(next(evens))
print(evens.__next__())


for x in evens:
    print(x)




