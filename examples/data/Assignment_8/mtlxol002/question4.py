"""CSC1015F Assignment 8 Question 4
Xola Matlanyane MTLXOL002
9 May 2014"""

import sys
sys.setrecursionlimit(30000)

#write palindromic-checks function for number (n) until the end point (e)
def paliprime(n, e):
    if n > e:
        return True              # if the recursion reaches the end point, terminate the recursion
    n=str(n)
    if pali(n) == True:
        if prime(int(n), 2) == True:   #if it's also a prime number, then print the number
            print(n)
    paliprime(int(n) + 1, e)
    
#write prime check function for a number (n) (including a counter (c))
def prime(n, c):
    if n == 1:             #if the number is a 1, then it is not prime
        return False
    if n == 2:
        return True        #if the number is a 2, then it is a prime
    if c > int(n**0.5)+1:  #use a prime check =, until it reaches the 1 more of the square of the number
        return True        #this ensures recursion doesn't continue on too deep
    if n%c == 0:           #if the number divides with a number cleanly, then it is not a prime
        return False
    if c == 2:        #dealt with even check, now moving on to odd check
        c += 1
    else:
        c += 2
    return prime(n,c)

def pali(s):
    if len(s) < 2:   #single digits are palindromes
        return True
    if s[0] != s[-1]:  #if the 2 ends are not equal, then it is not a palindrome
        return False
    return pali(s[1:-1])   #otherwise check the next 2 ends if they do equal

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
paliprime(n, m)
