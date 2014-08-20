"""A8Q4 - Palindromic Primes
5/3/2012
CRNKEE002"""

from math import sqrt
import sys
sys.setrecursionlimit (50000)

def main():
    """main function"""
    N = eval(input('Enter the starting point N:\n'))
    M = eval(input('Enter the ending point M:\n'))
    print('The palindromic primes are:')
    print_p_primes(N, M)

def is_palindrome(start, end, string):
    if string[start] != string[end]:
        return False
    elif start >= end:
        return True
    elif string[start] == string[end]:
        return is_palindrome(start +1, end -1, string)
    

def is_prime(number, divisor):
    if number % 2 == 0 and number !=2:
        return False        
    if divisor % 2 == 0:
        return is_prime(number, divisor-1)        
    if number==divisor:
        return is_prime(number, divisor-1)
    if divisor==1 or number==2:
        return True
    if (number % divisor==0):
        return False
    else:
        return is_prime(number, divisor-1)
     
def is_p_prime(number):
    if is_palindrome(0, len(str(number))-1, str(number)) == True:
        if is_prime(number, int(sqrt(number))) == True:
            return True
    return False

def print_p_primes(lowerlimit, upperlimit):
    if lowerlimit == upperlimit:
        if is_p_prime(upperlimit) == True:
            print(lowerlimit)
    else:
        if is_p_prime(lowerlimit) == True:
            print(lowerlimit)
            print_p_primes(lowerlimit+1, upperlimit)
        else:
            print_p_primes(lowerlimit+1, upperlimit)    
        

if __name__ == '__main__':
    main()