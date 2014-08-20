'''For primes that are palindromes, this will not be fun!'''

import sys
sys.setrecursionlimit (30000)
import math
check1=0


def prime(n,count,check):
    
    if count>= math.sqrt(n):#check this for all numbers below the squareroot of n
        
        return check
    elif n%count==0:#found a factor
        check +=1
        return prime(n,count+1,check)#if check is ever 2 or more, there was a factor
    else:#No factor found
        return prime(n,count+1,check)#n does not change because need it with a constant value


#yes palidrome works

check2 = True
def pali(name):
    #name = str(name)
    global check2
    
       
    #if check == False:
        #print(check)    
    if name == '' or len(name)==1:
        if check2== True:
            return('Palindrome!')
    elif name[0]!=name[-1]:
        #print(name[-1::-1])
        return('Not a palindrome!')
    else: 
        #print(name[-1], end='')
        return pali(name[1:-1])

#Now we have checked that it is a palindrome
def palrime(n,m):
    primeCheck = prime(n,1,0)
    #print(check1)
    if n==m+1:
            return False    
    elif primeCheck<=1:
        if pali(str(n))=='Palindrome!':
            print(n)
        return palrime(n+1,m)
    else:
        return palrime(n+1,m)
      
n =int(input('Enter the starting point N:\n') )
m =int(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
palrime(n,m)

        
    