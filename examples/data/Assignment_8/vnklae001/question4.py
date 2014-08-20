# Assignment 8 (Q4)
# A program that returns all palindromic primes between two integers supplied as input (start and end points are included)
# Written by: Laene van Niekerk
# VNKLAE001

import sys
sys.setrecursionlimit (30000)
import prime

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:\n", end="")

lst = []        # Empty is to append palindromes to
    
def palindrome(primes):     # Test to see if the prime number is a palindrome
    string = str(primes[0])
    reverse = string[::-1]
    if len(primes) == 1:    # If there is only one number
        if string == reverse:
            lst.append(primes[0])      
    elif string == reverse:     # If the number is a palindrome
        lst.append(primes[0])   # Appends number to list
        palindrome(primes[1:])  # Move on to rest of the list
    else:
        palindrome(primes[1:])  # If not palindrome, move onto next number
            
list_of_primes = prime.prime(n,m)
palindrome(list_of_primes)

for i in lst:
    print(i)