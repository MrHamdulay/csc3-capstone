#Mbongeni Mazibuko
#MZBMBO002
#Assignment 8

import math
import question1
import sys
sys.setrecursionlimit (30000)

count=0
def PalPrimes(n,m):
    '''higher function that receives 2 parameters'''
    global count
    '''variable defined out of function'''
    prime=0
    n=int(n)
    m=int(m)
    pal= question1.palindrome(str(n+count),0)
    '''uses palindrome function defined in question1'''
    if pal=='Palindrome!' and (1<n+count<=m):
        PalPrime(n+count,n+count-1)
        '''uses PalPrime to check if number is prime or not'''
        if n+count<=m:
            count+=1
            return PalPrimes(n,m)
    else:
        if n+count<=m:
            count+=1
            return PalPrimes(n,m)
       
def PalPrime(i,pri):
    ''' note function is PalPrime NOT PalPrimeS, PalPrimeS is higher function,
    PalPrime checks whether the parameter is a prime number or not'''
    if (i)%abs(i-pri)==0 and 1<abs(i-pri)<(i):
        '''closes when there is a divisor'''
        return 
    elif pri<(i//2):
        '''prints prime when there is no divisor'''
        return print(i)
    else: 
        pri-=1
        return PalPrime(i,pri)
    
n=input('Enter the starting point N:\n')
m=input('Enter the ending point M:\n')
print('The palindromic primes are:')
PalPrimes(n,m)