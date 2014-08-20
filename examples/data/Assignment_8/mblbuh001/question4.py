# question4.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 07 May 2014

import question1
import math
import sys
sys.setrecursionlimit (30000)

start = eval(input("Enter the starting point N:\n"))                #get input (starting number) from user
end = eval(input("Enter the ending point M:\n"))                    #get input (ending number) from user

def prime(num,div=2):
    if num < 2:
        return False                                                #if number is less than 2, return false - is not prime
    elif div > math.sqrt(num):
        return True                                                 #if number is not divisible by all factors up to its square root, return true - is prime
    elif num % div != 0:
        return prime(num,div+1)                                     #if number is not divisible by div, check if it is divisible by div+1
    else:
        return False                                                # if number is divisible by at least one factor less than its square root, return false - is not prime

def palin_primes(start,end):
    if start == end:
        if question1.palin(start) and prime(start,div=2):
            print(start)                                            #if number is palindromic and prime, print it out
    elif start < end:
        if question1.palin(start) and prime(start,div=2):
            print(start)                                            #if number is palindromic and prime, print it out
            return palin_primes(start+1,end)                        #checks if next number is also a palindromic prime
        else:
            return palin_primes(start+1,end)                        #checks if next number is a palindromic prime
    else:
        return palin_primes(end,start)                              #if start > end, start = end and end = start
            
print("The palindromic primes are:")
palin_primes(start,end)