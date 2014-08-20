"""Question 4-Assignment 8
FRNHAN004
5 May 2014"""

import math
import sys
sys.setrecursionlimit (30000)

n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))

def p_prime(n,m):
    if n>m: #if n,m are equal dont do anything 
        return ""
    else:
        if is_prime(n) and is_palindrome(n):
            return str(n) +"\n"+ str(p_prime(n+1,m)) #if number is both a palindrome and a prime, return number and check next number
        else:
            return str(p_prime(n+1,m)) #add 1 to n each recursion
            
def is_palindrome(x): #function to determine if number is a palidrome
    x=str(x) #convert int into string, for string split
    if len(x)<1: #base case
        return True
    else:
        if x[0]==x[len(x)-1]:
            return is_palindrome(x[1:len(x)-1])
        else:
            return False
    
def is_prime(z): 
    if z<=1:
        return False
    else:
        return prime(z,z-1) #z must be one number less than y

def prime(y,z): #function to determine if number is a prime
    if z==1:
        return True
    else:
        if y%z==0: #y is the number we checking z is the divisor
            return False
        else:
            return prime(y,z-1) #minus 1 from z each recursion
        
print("The palindromic primes are:\n", p_prime(n,m), sep="", end = '')

        
    
        
    
            
        