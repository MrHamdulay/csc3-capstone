#Palindromic Prime check between two intervals
#Done By Guy Green
#Question 4 Assignment 8

import question1
import sys
sys.setrecursionlimit (30000)
import math

#Asking for inut
N=input("Enter the starting point N:\n")
M=input("Enter the ending point M:\n")


def palPrime(s,nl):
   #Base Case
   if int(nl)<int(s):
      return 0
   else:
      if question1.palindrome(s): #Checking if it is a palindrome
         if isPrime(int(s),2): #checking if the Palindrome is prime
            print(s) #printing prime
            return(palPrime(int(s)+1,nl))#recursion
         else:
            return(palPrime(s+1,nl)) #Recursion
      else:
         s=int(s)
         return palPrime(s+1,(nl))#recursion
        

def isPrime(a,count): #Function checking prime
   if count>(math.sqrt(int(a))): #checking up til squareroot of numbe
      return True
   elif a==2:
      return True
   elif int(a)%count!=0:
      return isPrime(int(a),count+1)
   elif a<2:
      return False
   else:
      return False
   

if N=="1": #Was giving me problem #HARDCODING
   print("The palindromic primes are:")
   palPrime(2,M)   
else:
   print("The palindromic primes are:")
   palPrime(N,M)