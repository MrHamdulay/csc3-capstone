"""Prints palindrome prime numbers in a given range
Trevor Byaruhanga
09 May 2014"""

import sys
sys.setrecursionlimit (30000)
# requests for 1st point and if its equal to 1 add 1 to it.
start =eval(input('Enter the starting point N:\n'))
if start == 1 :
    start+=1
end= eval(input('Enter the ending point M:\n'))
#checks if the number in the range is prime
def prime(a, b):
    if (b>a**(1/2)):
        return True
    if a%b == 0 : 
        return False
    else:
        return prime(a,b+1)


def palindrome(s):
    #checks if the first letter equals the second
    if s[0] != s[-1]:
       # if it doesnt, print the phrase below.
       return False
       #if it does search through the second an second to last letter.
    elif not s[1:-1]:
       return True
    else:
       return palindrome(s[1:-1])



# checks if the numbers that are palindrome primes and if they are, it prints them.   
def palindrome_primes(a,b):
    if a> b:
        return''
    else :
        if palindrome(str(a)) and prime(a,2):
            print(a)
        palindrome_primes(a+1, b)


print('The palindromic primes are:')
palindrome_primes(start,end)
