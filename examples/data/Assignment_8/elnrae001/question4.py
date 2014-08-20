'''Find the palindrome primes in a list of numbers
Author:Raees Eland
Date:07 May 2014'''
import math
import sys
sys.setrecursionlimit (30000)

def pal(M): 
   '''reverses the numbers'''
   if M=='': 
      return M
   else:
      return M[-1] + pal(M[:-1])

def pal_prime(M,N):
   '''checks if number is a palindrome and a prime then returns the number''' 
   if M==N+1:
      return ''
   if prime(M, int(math.sqrt(M))): # executes if number is a prime
      if str(M)==pal(str(M)):
         return str(M)+'\n'+str(pal_prime(M+1,N))
      else:
         return str(pal_prime(M+1,N))
   else:
      return str(pal_prime(M+1,N))
         
def prime(M,N):
   '''Finds the prime numbers'''
   if M==1:
      return False
   if N==1:
      return True
   if N==0:
      return False    
   elif M%N==0 and M!=N:
      return False
   elif M%N!=0 and M!=N:
      return prime(M,N-1)
   else:
      return prime(M,N-1)

if __name__=='__main__':
   M=eval(input('Enter the starting point N:\n'))
   N=eval(input('Enter the ending point M:\n'))
   print('The palindromic primes are:')
   print(pal_prime (M,N))
   
   