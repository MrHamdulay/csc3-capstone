"""recursively finds palindromic prime numbers between two integers (inclusive)
jonathan nathan
7 may 2014"""

# hussein said so
import sys
sys.setrecursionlimit (30000)
import math

the_list=[]
"""adds numbers in range N to M to the_list"""
def number_list(N, M):
    # base case
    if N == M:
        the_list.append(N)
    # recursive step
    else:
        the_list.append(N)
        number_list(N+1,M)

        
def rreverse(s):
    """reverses a string supplied to it"""
    # base case
    if s == "":
        return s
    # recursive step
    else:
        return rreverse(s[1:]) + s[0]
    
    
palindromic_list = []       
def palindromic():
    """calculates whether a number is a palindrome and appends all palindromes to palindromic_list"""
    # base case
    if the_list == []:
        return
    # uses rreverse function to test for palindrome
    elif str(the_list[0]) == rreverse(str(the_list[0])):
        palindromic_list.append(the_list[0])
        the_list.pop(0)
        palindromic()
    elif str(the_list[0]) != rreverse(str(the_list[0])):
        the_list.pop(0)
        palindromic()
    
        
prime_list = []
def prime_check(start_factor):
    """appends prime palindromes in palindromic_list to prime_list"""
    # sets end_factor to the square root of the number
    if palindromic_list != []:
        end_factor = round(math.sqrt(palindromic_list[0]))
    # base case
    if palindromic_list == []:
        return
    if palindromic_list[0] == 2:
        prime_list.append(palindromic_list[0])
        palindromic_list.pop(0)
        prime_check(2)
    elif start_factor > end_factor:
        palindromic_list.pop(0)
        prime_check(2)
    elif palindromic_list[0] % start_factor == 0:
        palindromic_list.pop(0)
        prime_check(2)
    elif (palindromic_list[0] % start_factor != 0) and (start_factor < end_factor):
        prime_check(start_factor + 1)
    else:
        prime_list.append(palindromic_list[0])
        palindromic_list.pop(0)
        prime_check(2)
        
def print_palindromic_primes(i):
    """prints palindromic prime numbers"""
    # base case
    if prime_list == []:
        return
    else:
        print(prime_list[i])
        if i != len(prime_list) - 1:
            # recursive step
            return print_palindromic_primes(i + 1)
    
    
# gets integer 1 (N) from user
N = eval(input('Enter the starting point N:\n'))
# gets integer 2 (M) from user
M = eval(input('Enter the ending point M:\n'))

# function calls
number_list(N,M)
palindromic()
prime_check(2)
print("The palindromic primes are:")
print_palindromic_primes(0)