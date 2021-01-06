# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:55:51 2020

@author: Nishanth
"""

def numbergenerator():
    a=1
    b=2
    c=a+b
    return c
    return a

print(numbergenerator())

#==============================================

"""
In Function return is return only one values

Suppose you need to return mulitply values
That that using yiled
    when you use yiled that function is generators


real-world use case of yield

        Music Player - peause and play

"""

def numbergenerator():
    a=1
    b=2
    c=a+b
    yield c
    yield a

var1=numbergenerator()

#print(var1.__next__())
#OR

print(next(var1))
print(next(var1))

#==============================================


def greeted():
    a = "Welcome Man!"
    b = "Hello , How are you Man ?"
    c = "I'm Fine buddy"

    yield a
    yield b
    yield c

Gen=greeted()

print(next(Gen))

print(next(Gen))

print(next(Gen))

# Use for loop for printing generator
for gen in greeted():
    print(gen)

#==============================================


'''
memoryview module for monitor the memoery
'''

print("Using return ")
import memory_profiler
import time

def check_even(numbers):
    even=[]
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even



if __name__ == '__main__':
    m1 = memory_profiler.memory_usage()
    t1 = time.time()

    cubes = check_even(range(10000000))

    t2 = time.time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]

    print(f'It took {time_diff}Secs and {mem_diff} MB to execute this method')










print("Use yield")
import memory_profiler
import time

def check_even(numbers):
    even=[]
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even



if __name__ == '__main__':
    m1 = memory_profiler.memory_usage()
    t1 = time.time()

    cubes = check_even(range(10000000))

    t2 = time.time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]

    print(f'It took {time_diff}Secs and {mem_diff} MB to execute this method')













