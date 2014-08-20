"""Amy Bosworth
Assignment 8
Question 4
6 May"""

import math
import sys
sys.setrecursionlimit (30000)

# Get range
start= eval(input("Enter the starting point N:\n"))
end= eval(input("Enter the ending point M:\n"))


divNum= 2

def primes(start, divNum):
   # if it passes not being divisible then must be prime 
   if divNum>=start:
      return True
   elif start%divNum==0:
      return False
   else:
      return primes(start,divNum+1)
        
def palindrome(start):
   start=str(start)
   if len(start)==0 or len(start)==1:
      return True
   
   elif start[0] == start[-1] and palindrome(start[1:-1]):
      return True 
   else:
      return False 


def palinprime(start):
   if start>end:
      return ''
   if start==1:
      return palinprime(start+1)
   if primes(start, divNum)==True and palindrome(start)== True:
      return '\n' + str(start) + str(palinprime(start+1))
   else:
      return palinprime(start+1)

print("The palindromic primes are:",palinprime(start),end='')