# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:39:06 2022

@author: Steven Cheng
"""
# Use the file name mbox-short.txt as the file name

# This is my file "D:/Files/Python 4 Everyone/Assignments/mbox-short.txt"


fname = input("Enter file name: ")
fh = open(fname)
countline = 0
# SpamConfArray = []
SpamConfArray = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    # SpamConfArray.append(float(line[line.rfind(' ')+1:len(line)])) 
    SpamConfArray = SpamConfArray + float(line[line.rfind(' ')+1:len(line)])
    countline = countline + 1
    AvgSpamConf = SpamConfArray/countline
    
print("Average spam confidence:", AvgSpamConf)
    
