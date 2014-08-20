""" check for palandromic primes using recursion
kenneth mphele
5 may 2014"""


import sys
sys.setrecursionlimit (30000)
import math

divisor=1
def prime(number):
    global divisor
    if number==0:
        return True
    elif number==1:
        return True
    else:
        divisor+=1
        if number%divisor!=0:
           
            if divisor<math.sqrt(number):
                return prime(number)
            else:
                return True
        else:
            return False


def palidrome(number):
    number=str(number)
    if len(number)==0 or len(number)==1:
        return True
    else:
        if number[0]==number[-1]:
            return palidrome(number[1:-1])
        else:
            return False


def check(n,m):
    if n==m:
        return ""
    if prime(n)==True and  palidrome(n)==True:
            print(n)
            return check(n+1,m)
        
    else:
        return check(n+1,m)
    
n=input("Enter the starting point N:\n")
m=input("Enter the ending point M:\n")
print("The palindromic primes are:") 
print(check(n,m))
#print(prime(535))
        
        
    