"""Cherise Dube 
06 May 2014
Program to find all palindromic prime numbers between two input integers"""

import sys
sys.setrecursionlimit (30000)

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))


def reverse(s):
    """reverses a string"""
    if len(s)==0:
        return ""
    else:
        return reverse(s[1:])+s[0]
    
def palindrome(N,M):
    """Check if numbers are palindromes and creates a string of the numbers seperated by a comma"""
    if N<M:
        if str(N)==reverse(str(N)):
            return str(N)+" "+palindrome(N+1,M)
        else:
            return""+palindrome(N+1,M)
        
    elif N==M:
        if str(M)==reverse(str(M)):
            return str(M)+" "
        else:
            return ""

pal= palindrome(N,M) #Creates a string of the palindromes
        
def prime(pal):
    """Checks if numbers in palindrome list are prime numbers and returns them in a string"""
    
    if pal[0]==" ":
        if len(pal)==1:
            return ""
        else:
            return "\n"+prime(pal[1:])
        
    else:
        if ((2**(eval(pal[0:pal.find(" ")])))-2)%(eval(pal[0:pal.find(" ")]))==0:
            return pal[0:pal.find(" ")] + prime(pal[pal.find(" "):])
        else:
            return prime(pal[pal.find(" ")+1:])


print("The palindromic primes are:\n",prime(pal),sep="")
