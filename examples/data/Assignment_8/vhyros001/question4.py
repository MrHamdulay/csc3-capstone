"""Assignement 8 question 4 Find palindromic primes using recursion
Ross van der Heyde VHYROS001
7 May 2014"""

import math
import question1 # going to use rev() from question1
import sys
sys.setrecursionlimit (30000)

def isPrime(y, x):
    pri = True
    
    if x == 2 : return True    
    
    if x ==1:
        return False
    
    if x % y ==0:
        pri = False
    
    if y <= math.sqrt(x) and pri!= False:
        y+=1
        return isPrime(y,x)
    else:
        return pri
   
   
def isPalin(num):
    """Returns true if number is a palindrome"""
    if num == int(question1.rev(num)):
        return True
    else: 
        return False
   
def loop (s, e):
    if isPrime(2, s) and isPalin(s):
        print(s)
               
    #print("do stuff here",s)    
    if s < e:
        s+=1        
        loop(s,e)    


start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
loop(start, end)
#Enter the starting point N:
#200
#Enter the ending point M:
#800
#The palindromic primes are:
#313
#353
#373
#383
#727
#757
#787
#797