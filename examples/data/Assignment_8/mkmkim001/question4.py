""" Palindrome program that uses recurssion
    kimley
    07 May 2014"""
import sys
sys.setrecursionlimit (30000)
import math
m=eval(input("Enter the starting point N:""\n"))
n=eval(input("Enter the ending point M:""\n"))
print("The palindromic primes are:")

def prime (m,n,start):
    """find the prime number"""
    if m==n+1:
        return False
    elif m==2 or m==3:
        primes(m)
        return prime(m+1,n,2)
    elif m<2:
        return prime (m+1,n,2)
    elif m>3:
        if m%start!=0:
            if start<=(round(math.sqrt(m))+1):
                return prime (m,n,start+1)
            else:
                primes(m)
                return prime (m+1,n,2)
        if m%start==0:
            return prime (m+1,n,2)

def primes(number):
    strt=palicheck(number)
    if strt:
        print(number)
def palicheck(state):
    state=str(state)
    if len(state)==0:
        return True
    elif len(state)==1:
        return True
    elif state[0] == state[len(state)-1]:
        return palicheck(state[1:len(state)-1])
    else:
        return False
prime (m,n,2)