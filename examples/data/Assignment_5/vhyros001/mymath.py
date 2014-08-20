"""Assignment 5 question 3 
Ross van der Heyde VHYROS001
13 Arpil 2014"""

import math

def get_integer (a):
    print("Enter ", a,":", sep = "")
    b = input()
    while b.isdigit() == False:
        print("Enter ", a,":", sep = "")
        b = input()
    
    return eval(b)

def calc_factorial(a):
    return math.factorial(a)
    
#Enter n:
#4
#Enter k:
#2
#Number of permutations: 12