'''Question 4
Assignment 8
Tauriq Dolley

Write a program that calculates pallindromic primes within a designated range using recursion'''

import sys
import math
sys.setrecursionlimit (30000)

def reverse(word):
    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]
    
def isPrime(num,i):
        if num%i == 0 and num!=i or num == 1:            
            return False
        elif int(math.sqrt(num)) > i:
            return isPrime(num,i+1)
           
def pal_primes(n,m):
    if n == m:
        if str(n) == reverse(str(n)) and isPrime(n,2) == None:
            print(n)
    elif str(n) == reverse(str(n)) and isPrime(n,2) == None:
        print(n)
        return pal_primes(n+1,m)
    else: return pal_primes(n+1,m)
        
n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
primes = []
print("The palindromic primes are:")
pal_primes(n,m)      
    
    