# Question 4
# Richard van Gysen
# 8 may 2014
# Palindromic Primes between two numbers

import math

# increasing the limit of the number of recursions

import sys  
sys.setrecursionlimit(30000)

# function to find prime numbers
def Prime(x, counts): 
    if x == 1:
        return False
    elif counts == int(x**(1/2)) + 1: 
        return True
    else:
        if x % counts == 0:
            return False
        else:
            return Prime(x, counts + 1)
        
# reverse number check

def reverse(x): 
    return x if len(x) == 1 else x[-1] + reverse(x[:-1])

# palindrome check

def Palindrome(x):
    if str(x) == reverse(str(x)):
        return True
    else:
        return False
palindromes = ''

# if prime and palindrome, then print it

def palindrome_and_Primes(begin, finish):
    
    global palindromes
    if begin == finish: 
        if Prime(begin, 2) and Palindrome(begin):
            palindromes += str(begin)
    else:
        if Prime(begin, 2) and Palindrome(begin):
            palindromes += str(begin) + '\n'
            palindrome_and_Primes(begin + 1, finish)
        else:
            palindrome_and_Primes(begin + 1, finish)


n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindrome_and_Primes(n, m)
print(palindromes)