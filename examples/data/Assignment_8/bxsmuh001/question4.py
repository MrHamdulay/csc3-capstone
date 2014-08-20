#Assignment 8, Question 4
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 09/05/2014

#This program is designed find all the palindromic primes within a range.
#Pre-condition: Input range of numbers.
#Post-condition: Output palindromic primes.

#For this program, top down decomposition is used.

#This function is used to check if a string is a palindrome or not and returns True or False accordingly.
import sys
sys.setrecursionlimit(30000)

def isPalindromeAsString(a):
    a = str(a)
    if(len(a) == 1 or len(a) == 0 or a == " "): #If length of string is one or blank, it automatically is a palindrome.
        return True
    else:
        if(a[0] == a[-1]): #Checks if first and last characters are the same.
            return isPalindrome(a[1:-1]) #Runs loop again but without checking first and last character of a.
        else:
            return False
        
#Determine if a number is a palindrome.
def isPalindrome(a):
    return isPalindromeAsString(a)

#This function checks if a number is prime or not and returns True or False accordingly.
def isPrime(a,r=2): #a is the number that needs to be checked. r is the parameter which gets updated to check a.
    if (a == 2 or a==r):
        return True
    elif (a == 1 or a == 0 or a < 0):
        return False
    else:               
        if(a%r == 0):
            return False            
        else:
            return isPrime(a,r+1)    

#The main function that checks if a number is both prime and palindrome within range a and b.
def palimPrime(a,b):
    if(a == b):
        if(isPalindrome(a) and isPrime(a)): #If a equals b and if a is prime and palindrome, print(a).
            print(a)
        else:
            return False
    else:    
        if(isPalindrome(a)):           
            if(isPrime(a)): #If a is a Palindrome
                print(a) #If a is prime
        return palimPrime(a+1,b) #Check next number


#Checking if this file is being run as a standalone.
if __name__ == '__main__':
    userInputN = eval(input("Enter the starting point N:\n"))
    userInputM = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    if(userInputN == userInputM):
            if(isPalindrome(userInputN) and isPrime(userInputN)): #If a equals b and if a is prime and palindrome, print(a).
                print(userInputN)
    else:
        palimPrime(userInputN,userInputM)