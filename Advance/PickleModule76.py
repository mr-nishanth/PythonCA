# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:03:50 2021

@author: Nishanth
"""

import pickle

'''

Pickle is used for sequence data to Binary

'''

#cars=['audi','benz','BMW']

#file= "mycars.pkl" # file name

#fileobject = open(file, mode="wb")

#pickle.dump(cars,fileobject)

#fileobject.close()


cars=['audi','benz','BMW']

file= "mycars.pkl" # file name

fileobject = open(file, mode="rb")

print(pickle.load(fileobject))

fileobject.close()
