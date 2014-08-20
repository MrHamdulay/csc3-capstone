'''Palidrommic primes
Sbongakonke Mlangeni
07 April 2014'''



import math

import sys
sys.setrecursionlimit(30000)

start = eval(input('Enter the starting point N:\n'))
end = eval(input('Enter the ending point M:\n'))

def pal(start):  
   #stopping condition
    if str(start) == '':
        return str(start)
    #recursive step 
    else:
        return pal(str(start)[1:]) + str(start)[0]


div = 2
#prime checker
def prime(start,div):
    if str(start) == pal(start):
        if start == 1:
            return False
        if start == div:
            return True
        if start%div == 0:
            return False
        else:
            return prime(start,div +1)
        

#printing the output
print('The palindromic primes are:')
def palprime(start):
    global div
    global end
    
    #stopping condition1
    if start > end:
        return ''
    
    #stopping condition2
    elif start == 0:
        return ''
    
    #recursion step
    else:
        if prime(start,div) == True:
            print(start)
        return palprime(start + 1)
        
palprime(start)

