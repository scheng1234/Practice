# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:40:34 2023

@author: Steven Cheng
"""

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
lst = list()
count = 0
for line in fh:

    lst.append(line.rstrip())
    
for somestring in lst:
    
    if somestring.find("From ") == 0:
        print(somestring.split()[1])
        count += 1
        continue
    


print("There were", count, "lines in the file with From as the first word")
