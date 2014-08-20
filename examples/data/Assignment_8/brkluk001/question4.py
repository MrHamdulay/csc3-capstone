'''Program to calculate palindromic primes
8 May 2014
Luke Barker'''

import sys
sys.setrecursionlimit (30000)

def prime(x, divisor):       
    if x == divisor:      #base case
        return True
    elif x==1 or x==0:    #1 and 0 are not prime
        return False
    if x==2:              #2 is prime but divisible by 2 therefore needs seperate test
        return True
    elif x%2==0:          #if devisible by 2 not prime
        return False
    elif x%divisor ==0:   #if number divided divisor is 0 then return false 
        return False
    else:
        return prime(x, divisor +2)   #incease value of divisor

def palindrome(y):
    if len(y) <2:    #if a number is 1 digit then it is a palndrome
        return True
    if y[0] ==y[-1]:   #checks if the first digit equal to the last digit
        return palindrome(y[1:len(y)-1])   #repeats process recursively
    else:
        return False


def main(N,M):
    str_n = str(N)    #change number to string
    if N>M:
        return 
  
    elif prime(N,3) and palindrome(str_n):  #if number is both prime and palindrome print it
        print(N)
    return main(N+1,M)
    
    

N = eval(input("Enter the starting point N: \n"))
M = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
main(N,M)





    