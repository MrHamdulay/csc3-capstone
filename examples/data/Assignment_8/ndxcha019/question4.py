'''program to find palindromic primes
luke naude
08-05-2014'''

import sys
sys.setrecursionlimit(30000)

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))


def reverse(n):
    '''reverse number'''
    return n if len(n) == 1 else n[-1] + reverse(n[:-1])


def pal_check(n):
    if str(n) == reverse(str(n)):
        return True
    else:
        return False
    
def check_prime(n, count):
    '''check that the input is a prime'''
    if n == 1:
        return False
    elif count == int(n**(1/2)) + 1:
        return True
    else:
        if n % count == 0:
            return False
        else:
            return check_prime(n, count + 1)


palindromes = ''
def prime_pal(start, end):
    '''add palindromic primes to a list with \n to print each on a new line'''
    global palindromes
    if start == end:
        if check_prime(start, 2) and pal_check(start):
            palindromes += str(start)
    else:
        if check_prime(start, 2) and pal_check(start):
            palindromes += str(start) + '\n'
            prime_pal(start + 1, end)
        else:
            prime_pal(start + 1, end)



print("The palindromic primes are:")
prime_pal(n, m)
print(palindromes)