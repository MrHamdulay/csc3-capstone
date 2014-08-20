import sys
sys.setrecursionlimit (30000)
import math

# 10 May 2014
# Nikhil Gilbert
# Check for palindromic primes 

def prime(n,m):
    if n == 1:
        return False 
    elif m > math.sqrt(n):
        return True
    else:
        if n%m==0:
            return False
        else:
            return prime(n,m+1)

# more effectient way to check palindrome than previous programme, keeps input "whole"
def palindrome(x):
    if len(x) == 1:
        return x
    else:
        return x[-1] + palindrome(x[:-1])

def final(n,m):
    if n == m+1:
        return 
    elif n == 2:
        print (n)
    else:
        if prime(n, 2):
            if str(n) == palindrome(str(n)):
                print (n)
    return final (n+1,m)

#Prompts required for the programe and calling functions 
n = eval(input("Enter the starting point N:\n"))
if n: # ensures that programme has an input
    m = eval(input("Enter the ending point M:\n"))
    if m: # second measure to ensure that programme has an input 
        print ("The palindromic primes are:")
        final (n,m) 

    
