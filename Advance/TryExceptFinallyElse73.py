# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:40:22 2021

@author: Nishanth
"""

try:
    file = open("This.txt")
except Exception as e:
    print(e)

print("This Will Run")

#=========================================================

try:
    file = open("This.txt")
except Exception as e:
    print(e)

finally:
    print('This Will Always Execute')

    # every file finally closed
    #file.close()


print("This Will Run")



#=========================================================
'''
EOF Read Beyoud end of file
'''

try:
    file = open("this.txt")
except Exception as e:
    print(e)
except EOFError as eo:
    print(eo)
except IOError as io:
    print("This is a IO Error",io)


else:
    print("This will execute when except is not running")

finally:
    print('This Will Always Execute')

    # every file finally closed
    #file.close()

print("This Will Run")