'''Program that uses recursive functions to find all palindromic primes between two integers supplied as input
Daniel M. Tamale
TMLDAN001
2014-05-07'''

import math
import sys
sys.setrecursionlimit(30000)

number=eval(input('Enter the starting point N:\n'))
y=eval(input('Enter the ending point M:\n'))

def palindrome(number):
 '''To reverse number and check if its a palindrome'''
 if str(number)=='':
  return str(number)
 else:
  return palindrome(str(number)[1:])+str(number)[0]
 
factor=2
def Isprime(number,factor):
 if str(number)==palindrome(number):
  if number==1:
   return not True 
  elif number==factor:
   return True
  elif number%factor==0:
   return False
  else:
   return Isprime(number,factor+1)
  
print('The palindromic primes are:')
def main(number):
 global factor
 global y
 if number>y:
  return ''
 elif number==0:
  return ''
 else:
  if Isprime(number,factor)==True:
   print (number)
  return main(number+1)
main(number)