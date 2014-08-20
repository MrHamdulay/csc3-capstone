"""program to calc palinprimes between int
Claudia Pastellides 
9 May 2014"""

import sys 
sys.setrecursionlimit(30000) #allows recursion to be more accurate

def is_prime(prime, count): #checks for prime
    if prime == 1:
        return False
    elif count == int(prime**(1/2)) + 1:
        return True
    else:
        if prime % count == 0:
            return False
        else:
            return is_prime(prime, count + 1) #returns prime and adds 1 to count

def reverse(prime): #reverses
    return prime if len(prime) == 1 else prime[-1] + reverse(prime[:-1])
def is_palindrome(prime): #checks to palindrome
    if str(prime) == reverse(str(prime)):
        return True
    else:
        return False

palindromes = ''
def palindromic_primes(start, end): #palindrome primes between two points
    #defined for not only function but whole program
    global palindromes
    if start == end:
        if is_prime(start, 2) and is_palindrome(start):
            palindromes += str(start)
    else:
        if is_prime(start, 2) and is_palindrome(start):
            palindromes += str(start) + '\n'
            palindromic_primes(start + 1, end)
        else:
            palindromic_primes(start + 1, end)


n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindromic_primes(n, m) #starts function to determine palindrome prime
print(palindromes)
