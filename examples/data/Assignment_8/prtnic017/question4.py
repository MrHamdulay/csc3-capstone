# Student Number: PRTNIC017
# Date: 5/9/14

import sys
import math

sys.setrecursionlimit(30000)


def reverse_string(t):
    if len(t) <= 1:
        return t
    else:
        temp = ''
        if t[0] != ' ':
            temp = t[0]
        t = t.replace(t[0], '', 1)
        return reverse_string(t) + temp


def is_prime(value, dividor=2):
    if value % dividor == 0:
        return False
    elif dividor < round(math.sqrt(value),0):
        dividor += 1
        return is_prime(value, dividor)
    else:
        return True


def check_palindrome(current, end):
    if current == 2:
        print(2)
    elif current != 1 and str(current) == reverse_string(str(current)) and is_prime(current):
        print(current)
    current += 1
    if current <= end:
        check_palindrome(current, end)


starting = eval(input('Enter the starting point N:\n'))
ending = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
check_palindrome(starting, ending)