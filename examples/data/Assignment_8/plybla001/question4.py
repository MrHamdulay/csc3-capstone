"""Pallindromic Primes
B.Player
04/05/2014"""

import question1
import sys
import math
sys.setrecursionlimit(30000)

def prime(A,B):
   """checks for primes"""
   if A==1 or B==1: return False
   elif B>math.sqrt(A): return True
   elif A%B: return prime(A,B+1)
   else: return False
   

def palin_prime(M,N):
   """Returns a string with all the palindromic primes between M and N, inclusive"""
   if M==N:
      if question1.palin(str(M)): return str(M)
      else: return ""
   elif prime(M,2):
      if question1.palin(str(M)): return str(M)+" "+palin_prime(M+1,N)
      else: return palin_prime(M+1,N)
   else: return palin_prime(M+1,N)

M=eval(input("Enter the starting point N:\n"))
N=eval(input("Enter the ending point M:\n"))

lst=palin_prime(M,N).split()
print_str="\n".join(lst)
print("The palindromic primes are:\n"+print_str)


                  
         
  