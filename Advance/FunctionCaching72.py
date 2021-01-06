# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:08:55 2021

@author: Nishanth
"""

'''

Function Caching

'''

import time

def some_work(num) -> int:
    print("Calculating")
    time.sleep(2)
    return num*100


if __name__ == '__main__':
    print("Normal Function")
    var1=some_work(2)
    print(var1)

    var1=some_work(3)
    print(var1)

    var3=some_work(2)
    print(var3)


#=====================================================

import time
'''import functools
"least recently used"
@functools.lru_cache
'''

from functools import lru_cache

@lru_cache
def some_work(num) -> int:
    print("Calculating")
    time.sleep(2)
    return num*100


if __name__ == '__main__':
    print("Cache Function")
    var1=some_work(2)
    print(var1)

    var2=some_work(3)
    print(var2)

    var3=some_work(2)
    print(var3)


#=====================================================

import time

from functools import lru_cache
'''
lru_cache (maxsize=value) -> value is denote how many "least recently used"
memories in below example last var8 and var7 will be memories
'''

@lru_cache(maxsize=2)
def some_work(num) -> int:
    print("Calculating")
    time.sleep(2)
    return num*100


if __name__ == '__main__':
    print("Cache Function")
    var1=some_work(2)
    print(var1)

    var2=some_work(3)
    print(var2)

    var5=some_work(6)
    print(var5)

    var6=some_work(2)
    print(var6)

    var7=some_work(3)
    print(var7)

    var8=some_work(5)
    print(var8)

    var9=some_work(3)
    print(var9)



