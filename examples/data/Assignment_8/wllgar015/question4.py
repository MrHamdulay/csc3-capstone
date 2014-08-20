# Gareth Woolley

import sys #imports sys library
sys.setrecursionlimit(30000)


def is_prime(p, count): # checks if orime or not
    if p == 1:
        return False
    elif count == int(p**(1/2)) + 1:
        return True
    else:
        if p % count == 0:
            return False
        else:
            return is_prime(p, count + 1)


def reverse(p): #reverses the word
    return p if len(p) == 1 else p[-1] + reverse(p[:-1])


def is_palindrome(p):# checks if the word is a palindrome
    if str(p) == reverse(str(p)):
        return True
    else:
        return False


palindromes = ''
def palindromic_primes(start, end):
    # used for loop as recursion loop to not use while loop
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
palindromic_primes(n, m)
print(palindromes)