#Question 4
#Recursion ---->> Palindromic Primes
#RJDTAS001

import sys
import math
sys.setrecursionlimit (30000)


def reverser(number): 
    
    stringHandler=str(number)
    
    if stringHandler=="":
        
        return stringHandler 
    
    else:
        
        return (reverser(stringHandler[1:])+stringHandler[0]) 
    
    
    
def checkPrime(n, div=2):
    if n == 1:
        
        return False
    
    else:
        
        if div>math.sqrt(n): 
            
            return True
    
        if n%div==0: 
            
            return False
        
        else:
            
            div+=1
            
            return checkPrime(n,div)
    
    
def palindromePrimes(num1, num2):
    if(num1!=num2):
        
        if int(reverser(num1))==num1: 
            
            if checkPrime(num1):          
                return str(num1) + "\n"+ str(palindromePrimes(num1+1,num2))
            
            else:                
                return palindromePrimes(num1+1,num2)
            
        else:   
            return palindromePrimes(num1+1,num2)
        
    else:
        if int(reverser(num1))==num1:
            if checkPrime(num1):
                return num1      
        else:
            return ""
    
        
number1 = eval(input("Enter the starting point N:\n"))

number2 = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:\n"+palindromePrimes(number1,number2))