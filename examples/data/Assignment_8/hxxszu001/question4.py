# Annie
# 08 May 2014

import sys 
sys.setrecursionlimit(30000)


def primepos(p1, count): 
    if p1 == 1:
        return False
    elif count == int(p1**(1/2)) + 1:
        return True
    else:
        if p1 % count == 0:
            return False
        else:
            return primepos(p1, count + 1)


def reverse(p1): 
    return p1 if len(p1) == 1 else p1[-1] + reverse(p1[:-1])


def is_palindrome(p1):
    if str(p1) == reverse(str(p1)):
        return True
    else:
        return False


palindromes = ''
def palinprimes(beg, end):
  
    global palindromes
    if beg == end:
        if primepos(beg, 2) and is_palindrome(beg):
            palindromes += str(beg)
    else:
        if primepos(beg, 2) and is_palindrome(beg):
            palindromes += str(beg) + '\n'
            palinprimes(beg + 1, end)
        else:
            palinprimes(beg + 1, end)


x = eval(input("Enter the starting point N:\n"))
y = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palinprimes(x, y)
print(palindromes)