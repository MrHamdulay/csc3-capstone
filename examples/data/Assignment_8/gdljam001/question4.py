"""James Godlonton
Checking for palindromic primes
04 May 2014"""

import sys
import math
sys.setrecursionlimit (30000)

def main():
    """Input"""
    botVal=str(input("Enter the starting point N:\n"))
    topVal=str(input("Enter the ending point M: \n"))
    print("The palindromic primes are:")
    printPalPrime(int(botVal),int(topVal))

def printPalPrime(botVal,topVal):
    """Goes through palindromes between values, printing primes"""  
    if botVal==topVal+1:
        #If you reach the topVal+1 end 
        print("") 
    
    
    elif str(botVal)==str(botVal)[::-1]:
        #Checking if number is a palindrome
        if(botVal==1):#Skipping over 1
            printPalPrime(botVal+1,topVal)
            
        elif isPrime(2,botVal):
            #Checking if it is prime then print
            print(botVal)
            printPalPrime(botVal+1,topVal)#Go to next integer
            
        else:
            printPalPrime(botVal+1,topVal)#Go to next value...this one is not prime
    else:
        printPalPrime(botVal+1,topVal)#Go to next value...this one is not palindromic
            
        
        
    
def isPrime(count,num):
    """Checks if a number is prime"""
    if(count >math.sqrt(num)):
        #If you reach past root of num must be true
        return True
    elif(num%count==0):
        #If number is divible by int the not prime
        return False
    else:
        #If its not divisible then go to the next value
        return isPrime(count+1,num)
    
if __name__ =="__main__":
    main()
    


    