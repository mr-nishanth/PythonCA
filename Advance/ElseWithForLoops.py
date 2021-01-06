# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:31:47 2020

@author: Nishanth
"""

food = ['chappathi','rice','poori']
for item in food:
    print(item)
else:
    print("For Loop executed Successfully")



for two in range(1,21):
    if two%2 ==0:
        if two == 10:
            break
        print(two)
else:
    print("For loop executed successfully")



food = ['chappathi','rice','poori']
for items in food:
    if items == "burger":
        break
else:
    print("Your burger item not found")


food = ['chappathi','rice','poori']
for items in food:
    if items == "rice":
        print(items)
        break
else:
    print("Your burger item not found")


a="cured rice"
print(a.title())
print(a.capitalize())



mobile_list = ['nokia','readmi','realme','iphone']
user_selected = input("Enter the Choice : ").lower()

for item in mobile_list:
    if item == user_selected:
        print(f"Your {user_selected} order is ready in 5 mins")
        print("Thanks you!")
        break
else:
    print(f"Sorry Sir , {user_selected} is out of stack")






