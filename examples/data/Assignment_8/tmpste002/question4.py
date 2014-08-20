""" Recursive functions to find all palindromic primes between two integers supplied as input
(start and end points are included) """
__author__ = 'Stephen Temple'
__date__ = '2014/05/06'

import sys
sys.setrecursionlimit(30000)

palindromes = ''


def is_prime(p, start=2) -> bool:
    """ Check to see if a number, p, is a prime """
    if p == 1:
        return False
    elif start == int(p**(1/2)) + 1:
        return True
    else:
        if p % start == 0:  # start is a factor of n
            return False
        else:
            return is_prime(p, start + 1)


def reverse(p) -> str:
    """ Reverse a string """
    return p if len(p) == 1 else p[-1] + reverse(p[:-1])

# Check to see is a number, p, is a palindrome
is_palindrome = lambda p: True if str(p) == reverse(str(p)) else False


def palindromic_primes(start, end) -> str:
    """ Loop """
    global palindromes
    if start == end:
        if is_prime(start) and is_palindrome(start):
            palindromes += str(start)
    else:
        if is_prime(start) and is_palindrome(start):
            palindromes += str(start) + '\n'
            palindromic_primes(start + 1, end)
        else:
            palindromic_primes(start + 1, end)


if __name__ == '__main__':
    n = eval(input("Enter the starting point N:\n"))
    m = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    palindromic_primes(n, m)
    print(palindromes)