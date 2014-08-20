# BLKAT005
# Kate Bell
# 6 May 2014 

import math

#to increase the amount of recursion that Python will allow
import sys
sys.setrecursionlimit (30000)

def is_palindrome(s):
       """Test for palindrome"""
       if len(s)==1:
              return True
       elif len(s)==2:
              if s[0]==s[1]:
                     return True
              else:
                     return False
       elif s[0]==s[-1]:
              if is_palindrome(s[1:-1])== True:
                     return True
              if is_palindrome(s[1:-1])== False:
                     return False
       else:
              return False

def is_prime(num,m):
       """Test for prime"""
       if num==m:
              return True
       elif m<=num:
              if num%m ==0:
                     return False
              else:
                     return is_prime(num,m+1)
                  
def find_and_print(start,end):
       # recursive step    
       if start <= end:            
              if is_palindrome (str(start))==True:
                     if is_prime(start,2)==True:
                            print(start)              
              find_and_print(start+1,end)
   
# get start and end points from user              
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
if start <= end :
      find_and_print(start,end)
