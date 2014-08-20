# Author : Rayaan Fakier FKRRAY001
# Date : 24 - 03 - 2014
# Question 4

import math

def main():
    # Take inputs
    N = int(input("Enter the starting point N:\n"))
    M = int(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    # Loop through nums in boundaries
    for i in range(N+1,M,1):
        pr = True # Initially take i as a prime
        # For loop to check if not prime
        for j in range(2,int(math.sqrt(i)) + 1):
            if (i%j == 0):
                pr = False
        if pr: # When not not prime
            primestr = str(i)
            palin = primestr[::-1]
            if primestr == "1": # Removes 1
                continue
            if palin==primestr: # Check if number is a palindrome
                    print(i)
          
main()