# Question 4 Assignment 8
# James Behr
# 2014-05-05

from question1 import recursive_reverse
import math, sys

sys.setrecursionlimit (30000)

def is_prime(number, divisor = 2):
    if number == 1:
        return False
    if divisor > round(math.sqrt(number)):
        # If greater than square root, we don't need to test any more
        return True
    if number % divisor:
        return is_prime(number, divisor + 1)
    else:
        return False
    
def is_palindromic_prime(number):
    if is_prime(number) and str(number) == recursive_reverse(str(number)):
        # Check if string representation is the same as its reverse representation
        return True
    return False

def find_primes(number, end):
    if number == end:
        if is_palindromic_prime(number):
            print(number)
        return
    
    if is_palindromic_prime(number):
        print(number)
    find_primes(number + 1, end)
    
def main():
    print('Enter the starting point N:')
    start = int(input())
    print('Enter the ending point M:')
    end = int(input())
    print('The palindromic primes are:')
    find_primes(start, end)
    
if __name__ == '__main__':
    main()