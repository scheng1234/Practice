# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 00:11:08 2023

@author: Steven Cheng
"""


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lst = list()
hour = dict()

for line in handle:
    lst.append(line.rstrip().split())
    
for word in lst:
    
    if len(word) == 0: 
        continue
    else:
        if word[0].find("From") == 0 and len(word) > 2:
            hour[word[5][0:2]] = hour.get(word[5][0:2],0) +1
            
            
a = list(hour.items())
a.sort()

for k,v in a:
    print(k,v)
