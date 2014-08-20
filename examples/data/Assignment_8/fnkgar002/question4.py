"""Program to find palindrome primes
Gary Finkelstein
7 May 2013"""

#import functions to be used in program

import math

import sys
sys.setrecursionlimit(300000)

#get starting and end point values
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

#function to determine prime numbers
def prime(x,y): 
      
            if x < 2: 
                        return False
            elif x==2:
                        return True 
            else:
                        if x%y == 0: #not prime because divisle by number other thsan 1 or itself
                                    return False
                        elif x%y!= 0 and y!= 2: # if not divisle by number other thsan 1 or itself, check against number 1 less than y
                                    return prime(x,y-1)
                        elif y%x!= 0 and y==2: #number is prime
                                    return True
                        
def isPalindrome (word):
            if len(word) == 1 or len (word) == 0:  #if the word length is 1 or 0, then the word is a palindrome
                        return True
            if word[0] == word [-1]:               #if the first and last letters of the word are the same, then call the function again to repeat the process
                        if isPalindrome (word[1:-1]) == True:   
                                    return True
                        else:
                                    return False
            else:
                        return False        
#function to determine the palindrome primes using function created in question1 as well as this program
def palindromeprime(N,M): 
            if N > M:
                        return "" 
            else:
                        #determine if starting number is a palindrome
                        if isPalindrome (str(N))==True: 
                                    if prime(N,int(math.sqrt(N))+1)==True: #determining a prime
                                                return '\n' + str(N) + palindromeprime(N+1,M)
                                    else:
                                                return palindromeprime(N+1,M) # recall function to check next number if its a palindrome prime                                    
                        else:
                                    return palindromeprime(N+1,M) # recall function to check next number if its a palindrome prime
                      

print("The palindromic primes are:" ,palindromeprime(N,M),sep='',end='')
            
            