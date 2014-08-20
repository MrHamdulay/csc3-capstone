# Program prints palindromic primes between two given integers
# Wandile Lesejane
# 8 May 201420

import sys
sys.setrecursionlimit (30000)

N=input("Enter N\n")
def palindrome(N):
    if N=="":
        return N
    else:
        return palindrome(N[1:])+N[0]
   
def check_palindrome(N):   
    if N==palindrome(N[1:])+N[0]:
        return N
       
def prime(N):
    
    