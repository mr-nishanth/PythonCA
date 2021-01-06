# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:54:51 2020

@author: Nishanth
"""

print("Learn Generartors")
print(" Learn Iterable , Iterator and Iteration")

'''

Iterable   --   __iter__()
Iterator   --   __next__()
Iteration  --


'''

a = ["Cyber",21,99.77]
for i in a:
    print(i)



print("Background Process on Iterable object")
a="APPLE"
print(*(a.__iter__()))
print(list(a.__iter__()))


b=897654
print(*(b.__iter__())) # 'int' object has no attribute '__iter__'






