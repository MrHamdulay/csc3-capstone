''' a program that uses recursive functions to find all palindromic primes between two integers supplied as input 
sankara mallane
6 may 2014
'''
# increases the amount of recursions that python will allow
import sys

sys.setrecursionlimit (30000)

# import maths function
import math

# user input of the starting point
m=eval(input("Enter the starting point N:""\n"))

# user input of the ending point
n=eval(input("Enter the ending point M:""\n"))

# the palindromie primes
print("The palindromic primes are:")

# a funtion to check that it is a prime number as well as a palindrome
def primes(number):
    # check that the prime is a palindome
    strt=palicheck(number)
    if strt:
        print(number)

# a function to check if the integer is a palindome   
def palicheck(state):
    state=str(state)
    # check if the len is equal to 0
    if len(state)==0:
        return True
    # check if the length is equal to 1
    elif len(state)==1:
        return True
    # check that position 1 is equal to the length -1
    elif state[0] == state[len(state)-1]:
        return palicheck(state[1:len(state)-1])
    else:
        return False
    
# a function to check for the prime numbers between N and M
def prime (m,n,start):
    
    # check if m equals to n+1
    if m==n+1:
        return False
    # check if m equals to 2 or 3
    elif m==2 or m==3:
        primes(m)
        return prime(m+1,n,2)
    # check if m is less than 2
    elif m<2:
        return prime (m+1,n,2)
    # check if m is greater than 3
    elif m>3:
        if m%start!=0:
            if start<=(round(math.sqrt(m))+1):
                return prime (m,n,start+1)
            # pass statement through these conditions if it doesn't satisfy the above conditions
            else:
                primes(m)
                return prime (m+1,n,2)
        if m%start==0:
            return prime (m+1,n,2)


prime (m,n,2)