#Soham Hanuman Singh
#SNGSOH004
#Assignment 8
#Question 4


import sys
import math
sys.setrecursionlimit (30000)


def inverse(number): #function to reverse the input
    string=str(number)
    if string=="":
        return string #empty string
    else:
        return (inverse(string[1:])+string[0]) #using recursion to keep putting the first letter to the end of the word, returns the original word completely reversed
    
    
    
def isPrime(n, divisor=2):
    if n==1: #1 is not a prime number
        return False
    
    else:
        if divisor>math.sqrt(n): #if the divisor is greater than half the number
            return True
    
        if n%divisor==0: #if it is completely divisable by the divisor
            return False
        
        else:
            divisor+=1
            return isPrime(n,divisor)
    
    
def mainFunction(start, end):
    if(start!=end):
        
        if int(inverse(start))==start: #if the number is a palindrome
            
            if isPrime(start): #if the palindrome is a prime                
                return str(start) + "\n"+ str(mainFunction(start+1,end))
            
            else:                
                return mainFunction(start+1,end)
            
        else:   
            return mainFunction(start+1,end)
        
    else:
        if int(inverse(start))==start:
            if isPrime(start):
                return start      
        else:
            return ""
    
        
number1 = eval(input("Enter the starting point N:\n"))
number2 = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:\n"+str(mainFunction(number1,number2)))