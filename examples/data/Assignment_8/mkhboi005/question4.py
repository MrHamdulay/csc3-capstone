"""Tumi Mkhawana
6 May 2014
Assignment 8 question 4"""

import sys
sys.setrecursionlimit (30000)
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")


import question1
import math



def check_prime(N,prime):
    if prime <2:
        return False    
    elif N>math.sqrt(prime):
        return True
    elif prime%N!=0:
        return check_prime(N+1,prime)
    else:
        return False
    
def other(N,M):
    if N<=M:
        palin=question1.palin(str(N),0)=="Palindrome!"
        if  palin:
            if check_prime(2,N)==True:
                print(N)
        return str(other(N+1,M))
    else:
        return " "
                

print(other(N,M))
        

            