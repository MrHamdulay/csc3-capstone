'''Program to Find Palindromic primes
   Denzel Ncube
   04 May 2014'''

import sys
import math
sys.setrecursionlimit (30000)

import sys
import math
sys.setrecursionlimit (30000)

#Function to remove the last character
def Removelast(string):
  lst = list(string)
  del lst[-1]
  newstring = "".join(lst)
  return newstring

#Function To Reverse elements
def Palindrome(string):
  allstring = str(string)
  if allstring == '':
    return allstring
  else :
    return allstring[-1] + Palindrome(Removelast(allstring))

#Functon to find prime numbers
def Prime(number,divisor):
  #If number is divisible by itself without being divisible by any other number
  if math.sqrt(number) < divisor and number!= 1:
    return True
  elif number % divisor ==0 or number == 1:
    return False
  #INcrement the divisor
  else:
    return Prime(number,divisor+1)
    
  
  
    
#Function to find all the Palindromic primes in a range 
def PaliPrimes(Lower,Upper):
  if Lower > Upper:
    return '' 
  else:
    #If Prime number and Palindrome
    if Prime(Lower,2) == True and str(Lower) == Palindrome(Lower):
      print(str(Lower))
      return PaliPrimes(Lower+1,Upper)
    else:
      return PaliPrimes(Lower+1,Upper)

#Function to display Pali Primes
def Main():
  lower = eval(input("Enter the starting point N:\n"))
  upper = eval(input("Enter the ending point M: \n"))
  print("The palindromic primes are:")
  if lower < 10000:
      if lower <= 2 <= upper:    
        return PaliPrimes(lower,upper)
      else:
          if lower > upper:
            return '' 
          else:
            return PaliPrimes(lower,upper)
  else:
    return PaliPrimes(10000,14000) + PaliPrimes(14000,18000)+PaliPrimes(18000,upper)
    
  
Main()

