"""Assignment 8 Question4
Djavan Arrigone 9th May 2014"""

import question1
import sys
import math
sys.setrecursionlimit (30000)

def pal(n, m):
    if n <= m: #Base case. 
        if isprime(n, 2) and question1.palindrome(n) == True: #Condition checking if number is palidrome and is a prime number. 
            print(n)
        pal(n+1, m) #Recursion occurs sending next value. 


def isprime(start, div):
    if start == 2: #Two will always be prime. 
        return True
    elif math.sqrt(start) + 1 > div:
        if start % div == 0:
            return False
        else:
            return isprime(start, div +1)
    else:
        return True 
    

N = eval(input("Enter the starting point N: \n")) 
M = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
if N == 0 or N == 1: #his ensures that values 0, 1 entered by user are converted to 2, being the base case. 
    N = 2
pal(N,M)



       




