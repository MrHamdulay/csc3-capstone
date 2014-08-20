'''program to find all palindromic primes between 2 integers
Thabiso Beau
5 May 2014
Assignment 8: #question4.py'''

import sys
sys.setrecursionlimit (30000)

import math


#reverse program to test possible palindromes
def reverse(start):
    start = str(start)
    if start =='':
        return start
    else:
        return reverse(start[1:]) + start[0]
    
#palindrome program    
def palindrome(start):
    start = str(start)
    X = reverse(start)
    if start == '':
        return True
    elif eval(start)== eval(X):
        #variable = sqrt(start)
        return  True #in lieu of this, use prime(palindrome(start+1))
    else:
        return False
#palindrome(start+1)
#primality program
def prime(start, divisor):
    if start < 2:
        return False
    
    elif start == 2:
        return True
    elif math.sqrt(start) + 1 > divisor:
        if start % divisor == 0:
            return False
        else:
            return prime(start, divisor +1)
    else:
        return True 
    
def counter(start, end):
    if start <= end:
        if prime(start, 2) and palindrome(start):
            print(start)
        counter(start+1, end)

start = eval(input('Enter the starting point N: \n'))
end = eval(input('Enter the ending point M: \n'))    

print('The palindromic primes are: ')
counter(start, end)


#FIRSTLY: finding numbers that lie within the range
    #if start == '': #base case for induction to occur
        #return start
    #if start == end:
            #return start
    #else: 
        #return start+1
    
    
##def main(start, end):
    