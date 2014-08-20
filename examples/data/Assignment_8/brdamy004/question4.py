# Assignment 8 question 4
# Amy Brodie
# 8/05/2014

import math
import question1
import sys
sys.setrecursionlimit(30000)
         
# recursion function to find primes numbers 
def primes(x,start,end):
    if x == 1:
        flag = False
    elif (x%2 == 0) and (x != 2):
        flag = False
    elif (x%start == 0) and (x!=start):
        flag = False
    else:
        flag = True
    if flag == False:
        return flag
    elif start >= end:
        return flag
    else:
        return primes(x,start+2,end)
    

# recursion function to find the palindromic primes    
def palinprime(n,m):
    number_str = str(n)
    palindrome = question1.palindrome(number_str,len(number_str))
    if n > m:
        return ""
    elif primes(n,3,round(math.sqrt(n))+1) == True:
        if number_str == palindrome:
            print(n)
    return palinprime(n+1,m)
    
# get input from user and output the palindromic primes
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palinprime(N,M)