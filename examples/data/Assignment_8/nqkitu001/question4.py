"""Friday 9th May 2014
Itumeleng Nqoko
Assignment 8 Question4"""
#Program to find all palindromic primes between two integers
import math
import sys
sys.setrecursionlimit (30000)

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
def isprime(num,fact):
   if num==0 or num==1:
      return False
   elif num == 2:
      return True
   else:
      if (math.sqrt(num)+1)>=fact:
         if num%fact!=0:
               return isprime(num,fact+1)
         else:
               return False
      else:
         return True
   

def palindrome(num):
   string=str(num)
   if len(string)==0 or len(string)==1:
      return True
   else:
      if string[0]==string[(len(string)-1)]:
         return palindrome(string[1:(len(string)-1)])
      else:
         return False  

def palindrome_prime(N,M):
   if N<=M:
      if isprime(N,2) and palindrome(N):
         print(N)
         return palindrome_prime(N+1,M)
      else:
         return palindrome_prime(N+1,M)
palindrome_prime(N,M)
