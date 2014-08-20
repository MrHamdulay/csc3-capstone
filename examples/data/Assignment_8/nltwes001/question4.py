#ASSIGNMENT 5
#QUESTION 3
#NLTWES001

import sys
sys.setrecursionlimit (30000)

def reverse(teststring):
    if teststring=="":
        return teststring
    else:
        return reverse(teststring[1:]) + teststring[0]

def ispal(number):
    if str(number)==reverse(str(number)):
        return True
    else:
        return False

import math
def isprime(n, div=2):
    if n == 1:
        return False
    else:
        if div>math.sqrt(n): 
            return True
        if n%div==0: 
            return False
        else:
            div+=1
            return isprime(n,div)

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

def palprimes(N,M):
    if N<M:
        if ispal(N) and isprime(N):
                return str(N) + "\n" + str(palprimes(N+1,M))
        else:
            return palprimes(N+1,M)
    elif N==M:
        if ispal(N) and isprime(N):
            return str(N)        
        else:
            return ""
              
print("The palindromic primes are:")
print(palprimes(N,M))



    
        