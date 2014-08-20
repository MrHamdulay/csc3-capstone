#Shaylan Lalloo
#LLLSHA008

import sys
sys.setrecursionlimit(30000)

#check if it's a palindrome
def ispalin(x):
    x = str(x)
    if len(x) == 0 or len(x) == 1:
        #Same as question 1
        return True
    else:
        if x[0] == x[-1]:
            return ispalin(x[1:len(x) - 1])
        else:
            return False

def isprime(x, n):
    if x == 1:
        #if 1 then it's not a prime
        return False
    if n == 1:
        #if your loop variable is 1, then it's checked everything
        return True
    else:
        if x % n == 0:
            #if the loop variable divides, then it breaks and continue
            return False
        else:
            #otherwise decrease the loop variable and recall function
            return isprime(x, n - 1)

myout = []
#output array

def outprimes(low, hi):
    if hi < low:
        return
        #self explanatory
    else:
        if ispalin(hi):
            #if it's a palindrome, continue
            if isprime(hi, hi - 1):
                #if it's prime, then throw it in the answer
                myout.append(hi)
        outprimes(low, hi - 1)

n = int(input('Enter the starting point N:\n'))
m = int(input('Enter the ending point M:\n'))


print('The palindromic primes are:')

def pall():
    if len(myout) == 0:
        #if nothing to output, stop
        return
    else:
        print(myout[-1])
        #output last
        myout.pop()
        #delete it
        pall()
        #call again
        
outprimes(n, m)
pall()

