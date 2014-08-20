#Shivaan Motilal
#7/05/14
#Palindrome Prime

import sys
sys.setrecursionlimit (30000)
import math


N=eval(input("Enter the starting point N:\n"))

M=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")




def reverse(n):   # reverses string
   n=str(n)
   if n=="":
      return ""
   
   else:
      return reverse(n[1:])+ n[0]


          
def prime(n,i):
   
   if n<2:
      return False
   
   if n > i:
      
      if n % i == 0:
         
         return False                          
      
      
      else:
         i = i + 1
         return prime(n,i)
   else:
      return True

    
    
    
def ipalprime(N,M):
   
      if M==N:
            if str(N)==reverse(N) and prime(N,2):
                  print(N)
            else:
                  return
   
      elif str(N)==reverse(N) and prime(N,2):
            print(N)
            ipalprime(N+1,M)
   
      else:
   
            ipalprime(N+1,M)
                    

ipalprime(N,M)


