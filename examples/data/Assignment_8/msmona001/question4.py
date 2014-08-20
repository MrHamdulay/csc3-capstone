"""palindromic primes between two integers recursive function
Author: Onalerona Mosimege
04 May 2014"""

import math

import sys
sys.setrecursionlimit (30000)

def reverse(s):
    """reverse string to later check if palindrome or not"""
    #base case
    if s == "":
        return s
    #recursive case
    else:
        return reverse(s[1:]) + s[0]
    
i = 2
def not_prime(n):
    """checking whether a prime number or not: if not a prime number, will return true, else false"""
    #initialize i
    global i
    
    if (n ==1):
        return True
    elif (n == 2):
        return False
    elif (n % i == 0) and (i <= math.ceil(n**0.5)):
        return True
    elif (n % i ==0) and (i == n):
        return False
    elif (n % i != 0) and (i <= math.ceil(n**0.5)):
        i = i + 1
        return not_prime(n)
    elif (n % i != 0) and (i >= math.ceil(n**0.5)):
        return False    
    elif (n > i):
        i = i + 1
        return not_prime(n)
    
def palindrome(s):
    """checks whether palindrome or not: will return true if a palindrome"""
    if s == reverse(s):
        return True
    else:
        return False

string = "" #initialize string to be used

def pali_prime(m, n):
    global string
    global i 
    i=2
    """finds palindromic primes between m-start point and n-end point(inclusive)"""
    #base cases if n=m
    if (m==n) and (not_prime(int(m))== False) and (palindrome(m) == False) :
        return string
    elif (m==n) and (not_prime(int(m))== True) and (palindrome(m) == False):
        return string
   #recursive cases
    elif (m==n) and (not_prime(int(m))== False) and (palindrome(m) == True) :
        return string + m
    
    elif (not_prime(int(m)) == False) and (palindrome(m) == True):
        return string+ m + '\n' + pali_prime(str(int(m)+1), n)
   
    elif (not_prime(int(m)) == True) and (palindrome(m) == True):
        return string + pali_prime(str(int(m)+1),n)
    
    elif (not_prime(int(m)) == True) and (palindrome(m) == False): 
        return string + pali_prime(str(int(m)+1),n) 
    
    elif (not_prime(int(m)) == False) and (palindrome(m) == False):
        return string + pali_prime(str(int(m)+1),n)
    
    
    
   


n = input("Enter the starting point N:\n")
m= input("Enter the ending point M:\n")
print("The palindromic primes are:")
print(pali_prime(n,m))
    
        
    
    