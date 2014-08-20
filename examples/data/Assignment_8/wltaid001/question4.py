"""Aiden Walton
WLTAID001
Question 4 - Assignment 8"""
import sys
import math
sys.setrecursionlimit (30000)
def palindrome(n,base=0):
    if n == 0:
        return base
    else:
        return palindrome(n // 10, (base * 10) + (n%10))

def palindrome_prime(n,m):
    if n>m:
        return ""
    else:
        if isPrime(n,math.floor(math.sqrt(n))+1)==True and palindrome(n)==n:
            print(n)
            return palindrome_prime(n+1,m)
        else:
            return palindrome_prime(n+1,m)     
        
def isPrime(a,b):
    if a<2:
        return False
    if a==2:
        return True
    if b == 1:
        return True
    else:
        if(a % b == 0):
            return False
        else:
            return isPrime(a,b-1)
        
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindrome_prime(n,m)
