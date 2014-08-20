"""Program to Determine Palindromic Primes
Sithasibanzi Kondleka
9 May 2014"""

import math
import sys
sys.setrecursionlimit (30000)

#determine palindrome
def pal(string):
    if len(string) == 0:
        return "Palindrome" #a message that contains nothing is technically a palindrome
    if len(string) == 1:
        return "Palindrome" #a message that contains 1 letter is technically a palindrome
    if string[0] == string[-1]:
        return pal(string[1:-1])
    else:
        return "Not a palindrome!"

#determine prime number
def prime(number, divider):
    if number == 1:
        return "Not a prime" 
    if number == 2:
        return "Prime"
    if divider == 1:
        return "Prime"
    if number%divider == 0: #check if there's a remainder
        return "Not a prime"
    else:
        return prime(number, divider-1)
    
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))

#combine definitions for palindromes and prime numbers
def palPrime(n,m):
    if n > m:
        return ""
    else:
        divider = int(math.sqrt(n))+1
        if prime(n, divider) == "Prime":
            if pal(str(n)) == "Palindrome":
                print(n)
        return palPrime(n+1,m)
    
print("The palindromic primes are:")
palPrime(start, end)