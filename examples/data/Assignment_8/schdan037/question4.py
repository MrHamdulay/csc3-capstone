"""Daniel Schwartz
SCHDAN037
question 4 palindromic primes recursion
may 2014"""

import sys

sys.setrecursionlimit(30000)

i_unchanging = 2    # lowest prime check, unchanging

def is_prime(n, i):
    """recursive function checks if n is prime, i is iterative checker should always be 2"""
    if n == 2:                  # 2 is prime
        return True

    elif n < 2:                 # less then 2 or even not prime
        return False

    elif n % i == 0:            # divisible by 3 or greater not prime
        return False

    else:
        if int(n ** 0.5) + 1 == i:          # no divisor found then prime
            return True
        else:
            return is_prime(n, i + 1)          # recursive step


def is_palin(s):
    """recursive function to determine if string is a palindrome"""
    if s == "":
        return True
    if s[0] == s[-1]:
        return is_palin(s[1:-1])
    else:
        return False


def palin_primes(n, m):
    """checks if a number is a palindromic prime and prints it out if it is"""
    if n == m:
        if is_palin(str(m)):
            if is_prime(m, i_unchanging):
                print(m)

    elif is_palin(str(n)):
        if is_prime(n, i_unchanging):
            print(str(n))
            palin_primes(n + 1, m)
        else:
            palin_primes(n + 1, m)
    else:
        palin_primes(n + 1, m)


if __name__ == '__main__':
    n = int(input("Enter the starting point N:\n"))
    m = int(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    palin_primes(n, m)
