"""find all palindromic primes between two endpoints using recursion
Lauren Denny
8 May 2014"""

import sys
sys.setrecursionlimit(999999999)

import math

def palindrome(num):
    """return True if number is a palindrome and False if t is not"""
    num=str(num)
    if len(num)==1 or len(num)==0:
        return True
    elif num[0]==num[-1]:
        return palindrome(num[1:-1])
    else:
        return False    

def prime(num,divisor):
    """prime(num,2) returns True if num is prime and False if num is composite"""
    if num==1:
        return False
    if divisor>math.sqrt(num):
        return True
    else: 
        if num%divisor==0:
            return False
        else:
            return prime(num,divisor+1)
  
def pprimes(start,end):
    if start==end+1:
        return "" #Note to self: figure out how not to end off the list with an empty line
    else:
        if prime(start,2) and palindrome(start):
            return str(start) + "\n"+ str(pprimes(start+1,end))
        else:
            return pprimes(start+1,end)

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:\n",pprimes(start,end),sep="")

