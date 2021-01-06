# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:03:07 2021

@author: Nishanth
"""
import time

def searcher(name):
    book = " Hello Buddy ! I'm Nishanth "
    time.sleep(3)

    text = name
    if text in book:
        print("Your Results are found")
    else:
        print("Not found")

searcher("Nishanth")

#======================================================


import time

def searcher():
    book = " Hello Buddy ! I'm Nishanth "
    time.sleep(3)

    while 1:
        text = yield

        if text in book:
            print("Your Results are found")
        else:
            print("Not found")

'''
search.send('Buddy') ==> text = 'Buddy'
'''

search=searcher()
next(search)
search.send('Buddy')

search.send('Hello')

search.send("I'm")

search.send('Nishanth')


#======================================================

import time

def searcher():
    book = " Hello Buddy ! I'm Nishanth "
    time.sleep(3)

    while 1:
        text = yield

        if text in book:
            print("Your Results are found")
        else:
            print("Not found")

'''

Here searcher is function is store in search instance or variable

'''

search=searcher()
next(search)
search.send('Buddy')
input("Press Any Key : ")
search.send('Hello')
input("Press Any Key : ")
search.send("I'm")
input("Press Any Key : ")
search.send('Nishanth')


'''
Delete the corountines
'''
search.close() # StopIteration

next(search)
search.send("Buddy")

#======================================================
'''Again Start the co-rountines'''
import time

def searcher():
    book = " Hello Buddy ! I'm Nishanth "
    time.sleep(3)

    while 1:
        text = yield

        if text in book:
            print("Your Results are found")
        else:
            print("Not found")

'''

Here searcher is function is store in search instance or variable

'''

search=searcher()
next(search)
search.send('Buddy')
input("Press Any Key : ")
search.send('Hello')
input("Press Any Key : ")
search.send("I'm")
input("Press Any Key : ")
search.send('Nishanth')


'''
Delete the corountines
'''
search.close() # StopIteration

search=searcher()
next(search)
search.send("Buddy")


