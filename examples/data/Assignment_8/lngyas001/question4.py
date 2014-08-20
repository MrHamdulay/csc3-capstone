"""program to find palidromic primes betyween 2 integers
yasha longstaff
6 may 2014"""

import sys
sys.setrecursionlimit (30000)

def palin(s,x):
    if len(s)/2 >= x: #only work up to the middle
        if s[x] == s[-1-x] and palin(s, x+1) == 'Palindrome': #check first and last then do the rest of the word
            return 'Palindrome'
        else: #first and last values not =
            return 'Not a palindrome.'
    else:
        return 'Palindrome'


def prime()
    




n = eval(input('Enter the starting point N: \n'))
m = eval(input('Enter the ending point M: \n'))
print('The palindromic primes are:')
print(palin_prime(n,m))


               
    