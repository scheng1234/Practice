# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:18:05 2023

@author: Steven Cheng
"""

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 

print("There were", count, "lines in the file with From as the first word")
