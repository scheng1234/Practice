"""
Created on Fri Feb 17 09:17:13 2023

@author: Steven Cheng
"""

def function(roman):    

    ROMANS = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    x = list()
    j=0

    if len(roman) == 1:
        x.append(ROMANS[roman[0]])

    elif len(roman) > 1:
        for i in range(len(roman)-1):
            if ROMANS[roman[i]] - ROMANS[roman[i+1]] < 0:
                x.append((ROMANS[roman[i+1]] - ROMANS[roman[i]]))
                j=1
            elif j==1:
                x.append(0)
                j=0
            else:
                x.append(ROMANS[roman[i]])

        if j==0:
            x.append(ROMANS[roman[len(roman)-1]])
    return(sum(x))