# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:14:08 2021

@author: Nishanth
"""

import requests

url=requests.get("https://www.google.com/imgres?imgurl=https%3A%2F%2Fwallpaperaccess.com%2Ffull%2F1751257.jpg&imgrefurl=https%3A%2F%2Fwallpaperaccess.com%2Fcat-hd&tbnid=esv8E4FK9RfzhM&vet=12ahUKEwivxa6enofuAhUFQnwKHVC6BDEQMygAegUIARCxAQ..i&docid=vuDntS6FqoDcUM&w=1920&h=1200&q=cat%20hd%20wallpapers%201080p&ved=2ahUKEwivxa6enofuAhUFQnwKHVC6BDEQMygAegUIARCxAQ")

#print(url) # <Response [200]>

#print(url.text) # open Binary format

#print(url.content)


with open("Cat.jpg","wb") as Cat_file:
    Cat_file.write(url.content)
