'''Palindromic primes
Othniel KONAN
KNNOTH001
2014/05/04'''

from math import sqrt
import sys
sys.setrecursionlimit (30000)

def palindrome(nbr):
    '''Check if a number is a palindromic condidering it as a string
    it returns True if it's a palindrome and False if it's not'''
    if len(nbr) > 1:                                #set the breaking point when there is less than one character in the string
        if nbr[0] == nbr[len(nbr)-1]:               #If the first letter is the same as the last one
            return palindrome(nbr[1:len(nbr)-1])    #we go to check for the rest of the string
        else:                                       #if they're different
            return False                            
    else:                                           #if we get one or zero character a the end the it's a palindrome
        return True    


def prime(nbr,div):
    '''Check if a number is prime knowing that 'div' is the sqrt(nbr)
    return True if it's prime and False if ir's not'''
    if nbr==1 or nbr==0: return False   #define 1 and 0 as not being prime numbers
    if div > 1:                         #if the divisor is greater than one
        if nbr % div == 0:              #check for divisibility
            return False                #return false if the condition is satisfied
        else:
            return prime(nbr,div-1)     #we continue to check with a smaller divisor
    else: return True                   #if the divisor is one then we return True 


def pal_prim(N,M):
    '''print the number of palindromic primes between two number includng them'''
    if M >= N:                                                                  #if the last number is the biggest
        if palindrome(str(N)) == True and prime(N,round(sqrt(N))) == True:      #if the number is a palindromic prime
            print(N)                                                            #print he number
        return pal_prim(N + 1,M)                                                #check the next number
        
N = eval(input('Enter the starting point N:\n'))
M = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
pal_prim(N,M)