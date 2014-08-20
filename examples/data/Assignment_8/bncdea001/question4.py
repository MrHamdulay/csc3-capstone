#Program to find palendromic primes, using recursion
#Dean Bunce
#3 May 2014

import math

#Increase recursion limit
import sys
sys.setrecursionlimit (30000)


#Get endpoints
start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))

#Start dividing at 2 (divisor)
div=2

print("The palindromic primes are:")

#Find whether the number is a palindrome
def palindrome(number):
    
    number=str(number)
    
    if len(number)==1 or len(number)==0:
        
        return True
    
    #Check first and last letters recursively
    elif number[0]==number[-1]:
        
        return palindrome(number[1:-1])
    
    else: return False

#Find whether the number is a prime    
def prime(number,div):
    
    #If it has a factor other than a 1 and itself
    if (number!=2 and number%div==0) or number==1:
            return False 
     
    #Keep looking while the divisor is lower than the square root of the number 
    elif div<=math.sqrt(number) and (number%div!=0 or number==2):
        
        return prime(number,div+1)
    
    elif div>math.sqrt(number) and (number%div!=0 or number==2):
        return True
    
    
    
#Check for prime and palindrome and return results
def results(start,end):
    
    if prime(start,div)==True and palindrome(start)==True and start<=end:
        print(start)
        
        return results(start+1,end)
    
    
    elif start>end: 
        return ""
    
    else: 
        return results(start+1,end)
    

palindrome(start)
prime(start,div)
results(start,end)