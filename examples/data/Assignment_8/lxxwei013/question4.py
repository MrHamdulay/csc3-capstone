"""palindromic primes
Michelle Lu
7 May 2014"""

import math
import sys
sys.setrecursionlimit (30000)


def palindrome(number): #function from question 1. check if a number is a palindrome
        if len(number)<=1:
                return True
        elif number[0]==number[-1]: #if first digit == last digit
                return palindrome(number[1:-1]) 
        else:
                return False


def prime(number, factor): #check whether it is prime
        if number<2:
                return False
        if factor>math.sqrt(number): #if factor greater than square root of number, then it is a prime number.
                return True
        elif number%factor==0  and number>factor: #prime cannot have another factor besides 1 and itself
                return False
        else:
                return prime(number, factor+1) #recurses to find of there are any other factors


def palindromicprime(N,M):
        if N==M: #base case 
                if palindrome(str(N))==True: #checks whether if it is palindrome
                        if prime(N, 2)==True: #checks whether it is prime
                                print(N)
        else:
                if palindrome(str(N))==True:
                        if prime(N, 2)==True:
                                print(N)
                return  palindromicprime(N+1, M) #recurs next number

           
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))    
print("The palindromic primes are:")
palindromicprime(N,M)