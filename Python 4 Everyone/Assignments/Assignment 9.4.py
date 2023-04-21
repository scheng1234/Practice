# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:52:31 2023

@author: Steven Cheng
"""

name = input("Enter file:")

if len(name) < 1:

    name = "mbox-short.txt"

 

handle = open(name)

email_count = dict()

lst= list()

Memail = str()

count = 0

 

for line in handle:

    lst.append(line.rstrip())

 

for words in lst:

    

    if words.find("From ") == 0:

        email_count[words.split()[1]] = email_count.get(words.split()[1],0) + 1

        # if words.split()[1] not in email_count:

        #     email_count[words.split()[1]] = 1

        # else:

        #     email_count[words.split()[1]] += 1

 

for x in email_count:

    if email_count.get(x) > count:

        count = email_count.get(x)

        Memail = x

    else:

        continue

 

print(Memail, count)

        