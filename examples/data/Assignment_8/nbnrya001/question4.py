
import sys
import math
sys.setrecursionlimit (30000)


def inverse(number): 
    
    string=str(number)
    
    if string=="":
        
        return string 
    else:
        return (inverse(string[1:])+string[0])
    
    
    
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
    
    
def mainFunction(first, last):
    
    if(first!=last):
        
        if int(inverse(first))==first: 
            
            if isPrime(first):             
                return str(first) + "\n"+ str(mainFunction(first+1,last))
            
            else:                
                return mainFunction(first+1,last)
            
        else:   
            return mainFunction(first+1,last)
        
    else:
        if int(inverse(first))==first:
            
            if isPrime(first):
                
                return first      
        else:
            return ""
    
        
number1 = eval(input("Enter the starting point N:\n"))

number2 = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:\n"+str(mainFunction(number1,number2)))