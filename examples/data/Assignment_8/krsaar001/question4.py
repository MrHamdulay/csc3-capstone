# Aaron Krishna
# 9 May 2014
# A programs that finds all palindromic primes between two integers supplied as input

import sys
import question1
import math
sys.setrecursionlimit (30000)

def PrimeNumber(StartNumber, Divide): #function that checks if a number is prime
    if StartNumber < 2:
        return False
    elif StartNumber == 2:
        return True
    elif (math.sqrt(StartNumber) + 1) > Divide:
        if StartNumber % Divide == 0:
            return False
        else:
            return PrimeNumber(StartNumber, Divide +1)
    else:
        return True 
    
def counter(FirstNumber, LastNumber):
    if FirstNumber <= LastNumber:
        if PrimeNumber(FirstNumber, 2) and question1.PalinCheck(FirstNumber):
            print(FirstNumber)
        counter(FirstNumber+1, LastNumber)

FirstCheck = eval(input('Enter the starting point N: \n'))
LastCheck = eval(input('Enter the ending point M: \n'))    

print('The palindromic primes are: ')
counter(FirstCheck, LastCheck)