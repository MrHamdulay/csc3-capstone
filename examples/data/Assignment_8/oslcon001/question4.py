# Finds all palindromic primes between two integers
# Conor O'Sullivan
# 04/05/2014

import sys
sys.setrecursionlimit (30000)
import math

#Starting value
n = eval(input("Enter the starting point N:\n"))
#End value
m = eval(input("Enter the ending point M:\n"))

#main function
def main(n,m):
       if n>m:
              return 0
       elif palin(n) == True:
              if prime(round(math.sqrt(n)),n) == True:
                     print(n)
                     
              return main(n+1, m)
       else: 
              return main(n+1, m)
#Check to see if numbers are prime
def prime(div,num):

       if num == 1:
              return False
       elif div == 1:
              return True
       elif num%div == 0:
              return False
       else: 
              return prime(div-1,num)
#check if palindrom      
def palin(num):
       num = str(num)
       if len(num) == 1 or len(num) == 0:
              return True
       elif num[0] != num[len(num)-1]:
              return False
       else:

              return palin(num[1:len(num)-1])

print("The palindromic primes are:")
main(n,m)