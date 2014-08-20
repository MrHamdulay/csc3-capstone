"""recursive functions to find palindromic primes between two integers
Tim Hardie
9 May 2014"""

import sys
sys.setrecursionlimit (30000)

def check_palin (str_input):
    if len (str_input) > 1:
        if str_input[0] == str_input[-1]:
            check_palin (str_input[1:-1])
        else:
            return False
    elif len (str_input) == 1:
        return True
        
def check_prime ():
    #asdf
    
def palin_primes (n, m):
    #asdf

if __name__ == '__main__':
    n = eval (input ("Enter the starting point N:\n"))
    m = eval (input ("Enter the ending point M:\n"))
    print ("The palindromic primes are:")
    palin_primes (n, m)