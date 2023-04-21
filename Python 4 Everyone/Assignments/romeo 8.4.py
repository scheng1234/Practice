# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:57:11 2022

@author: Steven Cheng
"""

# r"D:\Files\Python 4 Everyone\Assignments\romeo.txt"

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:

    lst.append(line.rstrip().split())

    
c = list()
for word in lst:
    
    c = c + word
    
c.sort()
flist = c[:]
g = 0
for i in range(len(c)):

    x = i
    # print(i)
    if i == 0: continue

    if c[i-1] == c[i]: 
        g = g+1
        # print(x)
        del flist[x-g]
        continue

print(flist)



# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:

#     lst.append(line.rstrip())
    
# t = list()
# for word in lst:
    
#     t.extend(word.split())

# t.sort()
# print(t)
