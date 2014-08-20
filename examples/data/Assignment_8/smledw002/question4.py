#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014-05-09
#Function       : checks for palindromic primes
#Title          : Question4

import math
import sys

sys.setrecursionlimit(30000)


def iterator(start, end):
    """iterates over a set of values"""

    if str(start) == str(start)[::-1] and prime(start):
        print(start)
    if start < end:
        iterator(start + 1, end)


def prime(value, div=2):
    """checks if a values a prime number"""
    # 1 or less is not a prime
    if value <= 1:
        return False
    elif value == 2:
        return True
    elif value % div == 0:
        return False
    elif div < round(math.sqrt(value), 0):
        #optional variable div is used to iterate over possible factors
        return prime(value, div + 1)
    else:
        return True


start = eval(input("Enter the starting point N:\n"))
end_point = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
iterator(start, end_point)











