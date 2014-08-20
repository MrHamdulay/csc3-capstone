#Program that uses a uses a recursive function to check whether numbers are palindromic primes
#Saul Bloch
#7 April 2014

#importing functions to be used
import sys
import math
sys.setrecursionlimit(300000)

#Starting and ending points
Num1 = eval(input("Enter the starting point N:\n"))
Num2 = eval(input("Enter the ending point M:\n"))

#Function used in Q1 to check if palendrome
def isPalindrome (word):
    if len(word) == 0 or len (word) == 1:
        return True
    elif word[0] == word [-1]:
        if isPalindrome (word[1:-1]) == True:
            return True
        else:
            return False
    else:
        return False

#Function to check all prime numbers
def primeNumber(number1,number2):
    if number1 < 2: 
        return False
    elif number1==2:
        return True 
    else:
        #not a prime number as divisible by a number other than 1 and itself
        if number1%number2 == 0:
            return False
        elif number1%number2!= 0 and number2!= 2:
            return primeNumber(number1,number2-1)
        #Definition of a prime
        elif number2%number1!= 0 and number2==2:
            return True

#function to check and see if the the 2 functions (prime and palindrome) both return true
def palindromaticPrime(Num1,Num2): 
    if Num1 > Num2:
        return "" 
    else:
        #determine if starting number is a palindrome
        stringarised_num = str(Num1)
        #If palandrome ...
        if isPalindrome (stringarised_num)==True: 
            #if prime as well....
            if primeNumber(Num1,int(math.sqrt(Num1))+1)==True:
                return '\n' + stringarised_num + palindromaticPrime(Num1+1,Num2)
            else:
                #Recursion steps to check for palandromatic primes
                return palindromaticPrime(Num1+1,Num2)                                    
        else:
                return palindromaticPrime(Num1+1,Num2) 

print("The palindromic primes are:" ,palindromaticPrime(Num1,Num2),sep='',end='')

    
