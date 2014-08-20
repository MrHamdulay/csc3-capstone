#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     prints out all palendromic primes between two numbers
#
# Author:      Matthias
#
# Created:     05-05-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import sys
sys.setrecursionlimit (30000)

def is_prime(num, max_num):
    # num is the changing variable (starts at 2), while max_num is a constant
    # max_num is the number to be tested
    if max_num == 1:
        # 1 is not a prime number
        return False
    elif num > math.floor(math.sqrt(max_num)):
        # only have to check up to the squareroot of max_num to check if it is a prime
        return True
    elif max_num % num == 0:
        return False
    else:
        return is_prime(num+1, max_num)

def is_palindrome(string):
    if string == "":
        # basecase if the string is empty - indicates a palindrome
        return True
    if string[0] != string[-1]:
        # second basecase if first and last characters are not equal - not a palindrome
        return False
    return is_palindrome(string[1:-1])

def pal_primes(start, end):
    if start == end:
        # basecase
        if is_prime(2, start) and is_palindrome(str(start)):
            return str(start)
        else:
            return ""
    else:
        if is_prime(2, start) and is_palindrome(str(start)):
            # string all palendromic primes together, seperated by a new line
            return str(start) + "\n" + pal_primes(start+1, end)
        else:
            return pal_primes(start+1, end)

N = eval(input("Enter the starting point N: \n"))
M = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
print(pal_primes(N,M))