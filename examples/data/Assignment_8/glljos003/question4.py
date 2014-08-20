"""program to find palindromic primes in a given range
joshua gullan
5 may 2014"""

import sys 
sys.setrecursionlimit(30000) #sets recursion limit so system doesn't give error


def is_prime(x, count): #function checks if a number is prime or not
    if x == 1:
        return False  #1 is not a prime number
    elif count == int(x**(1/2)) + 1:  
        return True
    else:
        if x % count == 0:   #if number is divisable by any factor but one and itself, it is not prime
            return False
        else:
            return is_prime(x, count + 1)


def reverse_number(x): #reverses the number to determine if palindrome
    return x if len(x) == 1 else x[-1] + reverse_number(x[:-1])


def is_palindrome(x):
    if str(x) == reverse_number(str(x)): #if the reverse and the normal are the same, it's a palindrome
        return True
    else:
        return False


palindromics = ''
def palindromic_primes(start, end):
    global palindromics #global so it can change during recursive loop
    if start == end: 
        if is_prime(start, 2) and is_palindrome(start): #if the number is both prime and a palindrome
            palindromics += str(start)  #adding palindromic prime to string
    else:
        if is_prime(start, 2) and is_palindrome(start): #if the number is both prime and a palindrome
            palindromics += str(start) + '\n' #adding palindromic prime to string
            palindromic_primes(start + 1, end)  #move onto next iteration of recursive loop
        else:
            palindromic_primes(start + 1, end)   #move onto next iteration of recursive loop


n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindromic_primes(n, m)
print(palindromics)