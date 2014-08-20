"""Brandon Pickup"""
"""3 May 2014"""
"""Assignment 8 Question 4"""
"""program that uses recursive functions to find all palindromic primes between two integers supplied as input"""
import sys
sys.setrecursionlimit (30000)
n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
import math
def count_factors(counter,number):
    """function to count the number of factors from a starting value until the number itself"""
    if counter==int(math.sqrt(number))+1:#only check factors up to the sqaureroot of the number
        return 1
    elif number%counter==0:
        return 1+ count_factors(counter+1,number)
    else:
        return count_factors(counter+1,number)
def palindrome(s):
    if len(s)<=1:
        return True
    elif s[0] == s[-1]:#checks to see whether the first and last  are the same
        return palindrome(s[1:len(s)-1])#runs the function again on a string with either edge truncated
    else:
        return False
        
def pal_primes(n,m):
    """recursive function that prints numbers that are both prime and palindromic"""
    if n==m+1:#m+1 so that the m value is included in calculations
        return ""
    elif (palindrome(str(n)) == True and count_factors(1,n)<3 and n!=1) or n == 2:#conditions for a number to be both primes and palindromic - i.e. same forward and back, and less than 3 factors
        print(n)
        pal_primes(n+1,m)
    else:
        pal_primes(n+1,m)
print("The palindromic primes are:")
pal_primes(n,m)