'''Adam Rosendorff RSNADA001
03 May 2014
CSC1015F Assignment 8 Q4'''
import sys
import math
sys.setrecursionlimit(30000)
def palin(num):
    if len(num) <= 1:
        return True
    if num[0] == num[-1]: #checking first and last digits
        return palin(num[1:-1]) #number minus first and last digits
    return False

def prime(num,divider):
    if num <= 1:
        return False
    if divider == 1: # all num/divider had remainders, therefore prime
        return True
    if divider == 0: #dividing 1, 1 is not a prime
        return False
    if num % divider != 0: #checks if there is a remainder
        return prime(num,divider-1)
    return False
    
def primepals(start,end):
    if start == end+1:
        return ''
    if end < start:
        return ''
    if palin(str(start)) and prime(start,(math.sqrt(start)//1)):#only need to check factors up to sqrt(n)
        return str(start) + '\n' + primepals(start+1,end)
    return '' + primepals(start+1,end)
        
start = eval(input('Enter the starting point N:\n'))
end = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
print(primepals(start,end))
