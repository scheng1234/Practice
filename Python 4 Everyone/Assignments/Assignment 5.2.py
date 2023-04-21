# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:39:03 2022

@author: Steven Cheng
"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest is None or num > largest :
            largest = num
        elif smallest is None or num < smallest :
            smallest = num
    except: 
        print("Invalid input")
        

print("Maximum is", largest)
print("Minimum is", smallest)