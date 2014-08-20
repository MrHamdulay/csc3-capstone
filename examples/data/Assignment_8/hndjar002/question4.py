"""Program to check whether a number is a palindrome or not (Question 4)
Jaren Hendricks
8 May 2014"""

import sys
sys.setrecursionlimit (30000)


def palindrome_prime(n, m, p):
    if n > m:
        return p 
    else:
        if n <= m:
            p.append(n)
            #return palindrome_prime(n+1,m,p)
        
        P = n//10
        
        #if p[0] > 1:
        #if mod == 0 or P == 0    
        return palindrome_prime(n+1,m,p)

# input statements 
n = eval(input('Enter the starting point N:\n'))
m = eval(input ('Enter the ending point M:\n'))
print('The palindromic primes are:')

p = []

print(prime(n,m,p))
    


