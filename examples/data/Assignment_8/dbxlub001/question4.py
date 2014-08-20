"""Primes with a twist of fate
Lubalethu Dube
8 May 2014"""
import math 
import sys
sys.setrecursionlimit (30000)

def Mr_prime(num,factors):
    
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        if factors >= (math.sqrt(num))+1:
            return True
        elif num > 1:
            if num % factors == 0:
                return False
            else: 
                return Mr_prime(num,factors +1)
        else:
            return False

def Mr_Pally(number):
    if len(number) == 0 or len(number)== 1:
        return True
    elif len(number) == 2 and number[0] == number[1]:
        return True
    elif number[0] == number[len(number)-1]:
        return Mr_Pally(number[1:len(number)-1])
    else:
        return False
def Mr_pallyprime(lowest, highest):
    if Mr_prime(lowest,2):
        if lowest <= highest:
            if Mr_Pally(str(lowest)) == True:
                print(lowest)
                return Mr_pallyprime(lowest+1,highest)
            else:
                return Mr_pallyprime(lowest+1,highest)
    else:
        return Mr_pallyprime(lowest+1, highest)
    
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
Mr_pallyprime(N,M)
        

    
  
 
  