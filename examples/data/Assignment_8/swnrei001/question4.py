"""Question 4 of Assignment 8
produces all palindromic prime numbers between two bounds, (from user)
SWNREI001
05/05/2014"""

import math
import sys
sys.setrecursionlimit(30000)
# increase recursive limit to help recursive functions

def is_prime(num, check = 2):
    """Recursively checks if number num is a prime number by
    attempting check division with number 'check'"""
    if num == 1:
        return False
    elif check > math.sqrt(num):
        # base case: division checked up until sqrt of number to be checked
        return True 
    elif num % check == 0:
        # not a prime number if divisible by a lower number
        return False
    else:
        return is_prime(num, check + 1)

def reverse(string, acc = ""):
    """Recursively reverse 'string', storing results between recursions in 'acc'"""
    if string == "": # base case is empty string
        return acc
    else:
        # take first character from string and add to beginning of acc
        # ie in front of first character from previous recursion
        return reverse(string[1:], string[0] + acc) 

def is_palindrome(string):
    """Determines if a string is a palindrome by comparing it to its reverse
    string"""
    string_rev = reverse(string)
    return string_rev == string

def get_palin_primes(N, M):
    """Recursively generates a list of palindromic primes between starting value
    N and ending-value M"""
    # base case where N >= M
    if N > M: # strictly greater so endpoint is included
        return [] # return empty-list to keep within expected type
    else:
        # check if N is a prime and palindrome
        prime_list = [] # store N if N is a prime, else is empty
        if is_prime(N) and is_palindrome(str(N)):
            # if so, add to prime list
            prime_list.append(N)
        return prime_list + get_palin_primes(N + 1, M)

def print_list(l):
    """Recursively prints the elements of the list, l"""
    if l == []: # base case with nothing to print in list
        return
    else:
        # print first element and recur on rest
        print(l[0])
        print_list(l[1:])

def main():
    """Main function of module - gets start and end points from user, 
    generates and prints a list of palindromic primes between these values"""
    # get start and end points, N and M
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    # generate a list of primes between these points
    palprimes = get_palin_primes(N, M)
    # print the list
    print("The palindromic primes are:")
    print_list(palprimes)

if __name__ == "__main__":
    main()