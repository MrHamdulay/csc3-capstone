""" Program that returns palindromic prime numbers
Aubrey Baloi
08 May 2014"""

import sys
sys.setrecursionlimit (30000)


#Checking palindromes
def palindrome(string_no):
    if len(string_no) <= 1 :
        return True
    else :
        if string_no[0] == string_no[len(string_no)-1]: 
            return palindrome(string_no[1:len(string_no)-1])
        else:
            return False

# Checking primes
def prime_numbers (a, b):
    if (b>a**(1/2)):
        return True
    if a%b == 0 : # if it is divisible by b, then is not a prime
        return False
    else:
        return prime_numbers(a,b+1)
    
 # Checking palindromic prime numbers   
def palindro_primes(a,b):
    if a> b:
        return
    else :
        if palindrome(str(a)) and prime_numbers(a,2):
            print(a)
        palindro_primes(a+1, b)

a =eval(input('Enter the starting point N:\n'))
if a == 1 :
    a+=1
b= eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
palindro_primes(a,b)