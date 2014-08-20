"""Chris Bolton 11/05/2014 Question 4"""

import sys
import math
sys.setrecursionlimit (30000)


def reverse(number): 
    
    string=str(number)
    
    if string=="":
        
        return string 
    else:
        return (reverse(string[1:])+string[0])
    
    
    
def isPrime(n, divisor=2):
    
    if n==1:
        
        return False
    
    else:
        if divisor>math.sqrt(n): 
            return True
    
        if n%divisor==0: 
            return False
        
        else:
            divisor+=1
            return isPrime(n,divisor)
    
    
def combined(first, last):
    
    if(first!=last):
        
        if int(reverse(first))==first: 
            
            if isPrime(first):             
                return str(first) + "\n"+ str(combined(first+1,last))
            
            else:                
                return combined(first+1,last)
            
        else:   
            return combined(first+1,last)
        
    else:
        if int(reverse(first))==first:
            
            if isPrime(first):
                
                return first      
        else:
            return ""
    
        
nbr1 = eval(input("Enter the starting point N:\n"))

nbr2 = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:\n"+str(combined(nbr1,nbr2)))