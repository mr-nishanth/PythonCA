# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:43:26 2021

@author: Nishanth
"""

import os

''' Object Intro Fixtion '''
#print(dir(os))
#print(os.__dir__())


'''get current working directory'''
print(os.getcwd())

'''change directory'''

os.chdir("<path>")

print(os.getcwd())


print(os.listdir())

print(os.listdir("<path>"))


'''mkdir = make directory'''
os.mkdir("<floder>")

'''mkdir = make directorys'''
os.mkdirs("<floder>/<sub-floder>")


'''os.rename('old-file',new-file) rename the file '''
os.rename('old-file_name','new-file_name')


print(os.path.exists("ComPython/Advance"))
print(os.path.exists(r"F:\vscodelearn\learnpython\CodingAnna\ComPython\Advance"))
print(os.path.isdir("ComPython/Advance"))
print(os.path.isdir(r"F:\vscodelearn\learnpython\CodingAnna\ComPython\Advance"))














