''' This programm prints out the palindromic primes
Nxumalo Goodman
09 May 2014'''

import sys
sys.setrecursionlimit (30000)

import math
#prompt the user to enter the starting and ending values
strt=eval(input('Enter the starting point N:\n'))
end=eval(input('Enter the ending point M:\n'))

#checks if the number is a palindrome or not
def pal(num):
    num = str(num)
    
    if len(num) == 1 or num == '':
        return True
    elif num[0] != num[-1]:
        return False
    else:
        return pal(num[1:-1])

#checks if the number is a prime or not
def pri(strt,s):
    if strt == 1:
        return False
    elif s>math.sqrt(strt):
        return True
    elif strt%s == 0:
        return False
    else:
        return pri(strt,s + 1)


#checks if the palindrome is a prime or not
def Palpri(strt,end):
    if strt > end:
        print('')
    elif pal(strt):
        if pri(strt,2):
            print(strt)
            Palpri(strt + 1,end)
        else:
            return Palpri(strt + 1,end)
    else:
        return Palpri(strt + 1,end)
    
#prints out the palindromic primes
print('The palindromic primes are:')
Palpri(strt,end)