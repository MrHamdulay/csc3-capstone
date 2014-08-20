#program to generate palindromic primes in a given range
#Anthony Jacob
#09 May 2014

import sys, math
sys.setrecursionlimit (30000)#Set recursion limt


from math import *

def palin_Check(num) :#Same function converted from question one
    num = str(num)
    if len(num) == 1 or len(num) == 0:
        return True
    else :
        if num[0] != num[-1] :
            return False
        else:
            return palin_Check(num[1:len(num) - 1])
        
def is_prime(num,k):
    if num <= 1:
        return False
    elif math.sqrt(num) < k: #If the squareroot is exceeded number must be a prime because one half of factors exhausted
        return True
    elif num%k == 0 :
        return False #If divisible not a prime
    else:
        return is_prime(num,k+1) #Recall function to check whether num is divisible by the next value of k

a = int(input('Enter the starting point N:\n'))
b = int(input('Enter the ending point M:\n')) #Asking user for input

print('The palindromic primes are:')

def output(start, end) : #Recursive function to replace a loop for output
    if start > end :
        return 
    else:
        if palin_Check(start):
            if is_prime(start,2): #Call the previous functions to check whether a num in the entered interval is a palindrome and prime
                print(start)
        output(start+1,end)
        
output(a,b)    #calling function