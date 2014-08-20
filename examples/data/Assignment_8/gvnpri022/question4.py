
"""Question 4 - Assignment 8- check for prime palindromes using recursion
GVNPRI022- Prinesan Govender
09 May 2014"""
import sys
import math
sys.setrecursionlimit (30000)

begin= eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))


def checkPalindrome(num): #uses function from question1 to cehck pailindrome
    if len(num)<=1: #base case
            return True
        
    else:
        if num[0]==num[-1]: #if first and last letters equal
            return checkPalindrome(num[1:-1]) #call function again
            
        else:
            return False #if not equal - not a palindrome    



def checkPrime(num2, divisor):# to check if prime
    
    if num2==0 or num2==1: #base case-automatically not a prime
        return False
    
    else:
              
        if divisor>math.sqrt(num2): #uses theorem wherbey if the divisor of a number is greater than the square root it is prime
                    return True                    
        elif num2%divisor==0: #composite number
            return False             
        else:
            return  checkPrime(num2,divisor+1)
    
    
def repeat(begin, end): 
    if (begin== end+1): 
        return 
    else:
        if checkPalindrome( str(begin) ) == True: #convert string because checkPalindrome only works with string
            if checkPrime(begin,2) == True:  
                print(begin)               
        return repeat(begin+1,end) #move to next number in the range

print("The palindromic primes are:")
repeat(begin,end)