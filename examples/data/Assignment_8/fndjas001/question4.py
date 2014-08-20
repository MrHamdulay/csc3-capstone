"""A program to find all the palindromic primes between two numbers
Jason Findlay
09/05/2014"""

import sys
sys.setrecursionlimit(30000)

def palindrome(s):
    #Base case
    if len(s)<=1:
        return True
    else:
        k=s[0]
        l=s[-1]
        #Checks if paired characters match
        if k==l:
            return palindrome(s[1:-1])
        else:
            return False

def prime(num1,num2):
    if num1==1:
        return False
    elif num1==num2:
        if palindrome(str(num1)):
            print(num1)
    elif num1%num2==0:
        return False
    else:
        prime(num1,num2+1)

def counter(N,M):
    if N==M:
        prime(N,2)
    else:
        prime(N,2)
        counter(N+1,M)

N=int(input("Enter the starting point N:\n"))
M=int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

counter(N,M)
