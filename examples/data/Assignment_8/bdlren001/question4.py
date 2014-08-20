# Program that returns palindromic prime numbers
# Budeli Rendani
# BDLREN001
# 07/05/2014

import math
import sys
sys.setrecursionlimit(30000)

def prime (x, y): # Checking primes
    if (x%y==0 and x!=2 and x!=1):
        return False 
    else:
        if (y<math.sqrt(x)):
            return prime(x,y+1)
        else:
            return True

def palindrom_pr(x,y): # Checking palindromic prime numbers
    if x> y:
        return
    elif x*2>y*2:
        return
    else:
        if palindrom(str(x)) and prime(x,2):
            print(x)
    palindrom_pr(x+1, y)

def palindrom(string): #Checking palindromes
    if len(string) <= 1 :
        return True
    else:
        if string[0] == string[-1]: 
            return palindrom(string[1:-1])
        else:
            return False
    
x =eval(input('Enter the starting point N:\n')) # user enter the start point
if x == 1 :
    x+=1

y= eval(input('Enter the ending point M:\n')) # user enter the end point
print('The palindromic primes are:')

palindrom_pr(x,y)