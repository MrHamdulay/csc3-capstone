# find all palindromic primes in a specified range using recursion only
#victor gueorguiev
#03 May 2014


import sys
import math
sys.setrecursionlimit (300000)

def check_prime(x,counter): #counter should be assigned the value of x - 1
    if x < 2:
        return False
    elif counter == 1:
        return True
    elif x % counter == 0: 
        return False
    else:
        return check_prime(x,counter-1)

def is_prime(x):
    return check_prime(x,round(x/2)) #or change this back to x-1

def rec_palin(n):
    if n == '':
        return True
    elif n[0] != n[len(n)-1]:
        return False
    elif n[0] == n[len(n)-1]:
        return rec_palin(n[1:len(n)-1])

def is_palindrome_prime(startpoint,endpoint):
    if startpoint == endpoint+1:
        print(end='')
    elif rec_palin(str(startpoint)) and is_prime(startpoint):
        print(startpoint)
        is_palindrome_prime(startpoint+1,endpoint)
    else:
        is_palindrome_prime(startpoint+1,endpoint)
    
def main():
    n = eval(input('Enter the starting point N:\n'))
    m = eval(input('Enter the ending point M:\n'))
    print('The palindromic primes are:')
    is_palindrome_prime(n,m)
    
main()    
    