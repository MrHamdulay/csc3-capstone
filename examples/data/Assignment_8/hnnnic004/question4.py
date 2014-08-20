'''program to find palindrome primes using recursion
nicole henning
due 9 may'''

import math
import sys
sys.setrecursionlimit(30000)

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

num = N
list_palindrome = []
list_prime = []
index = 0

print("The palindromic primes are:")

def palindrome_str(string):
    if len(string) < 2: #if word contains only one or no letters/characters,true
        return True
    elif string[0] == string[-1]: #if end and beginning character are the same, true
        #make string now without first and last character, if they were equal
        return palindrome_str(string[1:-1]) #recursion - continue until not the same, or until length < 2
    else:
        return False    

def palindrome_int(num):
    if N <= num <= M:
        string = str(num)
        if palindrome_str(string) == True:
            print(num)
            return palindrome_int(num+1)
        else: 
            return palindrome_int(num+1)
        
        
palindrome_int(num) 