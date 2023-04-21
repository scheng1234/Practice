# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:20:12 2023

@author: Steven Cheng
"""
import re


name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1696462.txt"
#    name = "regex_sum_42.txt"
handle = open(name)


lst = list()

for line in handle:
    lst.append(line.strip())
    
regextxt = " ".join(lst)
    
# re.search('[0-9]+', lst[7])
lstofnum = re.findall("[0-9]+", regextxt) # Generates a list of numbers that were selected from the string.
lstofnum = [int(x) for x in lstofnum]

print(sum(lstofnum))

print( sum( [ int(x) for x in re.findall('[0-9]+',open("regex_sum_1696462.txt").read()) ] ) )
