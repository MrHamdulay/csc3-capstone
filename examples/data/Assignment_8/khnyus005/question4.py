'''
Created on 06 May 2014
Palindromic prime searching with recursion
@author: Yusuf Khan
KHNYUS005
'''
import sys
sys.setrecursionlimit(30000)#increase recursion limit

def palin(n,m):
    if n<=m:#checks in range
        if str(n)==(reverse(str(n))):#checks if palindrome
            if is_prime(n)==True:
                print(n)#if prime, print number
        return palin(n+1,m)#recursion
    else:
        return ''
    
def reverse(str1ng):#function to reverse string to be compared to original
    last = str1ng[-1::]#last char assigned to variable
    str1ng = str1ng[0:-1:1]#last letter of string removed
    if last == '':#if no chars left
        return ''#stop recursion
    else:
        return (last + reverse(str1ng))#recursion
    
def is_prime(n):#checks if input is prime
    if n < 2:
        return False
    if n in (2, 3, 5, 7):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_divisor = int(n ** 0.5) # square root of n
    divisor = 5#common, efficient prime searching algorithm until here
    return priming(n, divisor, max_divisor)#recursion loop in other method

def priming(n, divisor, max_divisor):#recursion loop
    if n % divisor == 0 or n % (divisor + 2) == 0:
        return False#checks for factor
    elif divisor >= max_divisor:
        return True
    else:#recursion
        return (False+(priming(n, divisor+6, max_divisor)))

n = eval(input('Enter the starting point N:\n'))
m = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
palin(n,m)#input, output and function calling