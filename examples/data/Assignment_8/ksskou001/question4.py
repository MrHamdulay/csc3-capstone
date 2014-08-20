'''The entire module prints out the palindromic prime numbers 
between two given numbers
By Hermann KOUASSI: KSSKOU001
On 05 May 2014'''

import math
import sys
sys.setrecursionlimit (30000)

def pal (nbr):
    '''returns True if number is palindromic, otherwise False'''
    #converts number to string
    nbr=str(nbr)
    #consider empty input as palindromic as well as all the one digit numbers
    if len(nbr)==0 or len(nbr) == 1:
        return True
    #stopping condition when string is two or 3 digits
    elif len(nbr)==2 or len(nbr)==3:
        #palindromic if first and last digits are the same, return true
        if nbr[0]==nbr[-1]:
            return True
        #otherwise return false
        else: return False
    #when string is more than 3 digits compare first and last digits
    else:
        #continue recursion with last two digits out if they are identical
        if nbr[0]==nbr[-1]:
            return pal(nbr[1:len(nbr)-1])
        #otherwise return False as not palindromic
        else:
            return False
        

def prime (nbr, divisor):
    '''returns True if a given number is a prime number and False otherwise'''
    
    #1 and 0 zer0 are are not prime
    if nbr == 1 or nbr == 0:
        return False 
    #stopping condition
    if divisor == 2 :
        #not a prime if number divisible by 2 and number other than 2
        if nbr % divisor == 0 and divisor != nbr:
            return False
        #otherwise number is prime
        else:
            return True
    #if divisor is greater than 2 
    else:
        # not prime if number divisible by any number other than 1 and itself
        if nbr % divisor == 0:
            return False
        #otherwise carry on checking if any divisor will be found reducing divisor by one until it stops when divisor equal 2
        else:
            return prime (nbr,divisor-1)
        

def pal_prime (start,end):
    '''check if both conditions are met and thereafter print or not number'''
    
    #create a variable divisor to pass it to prime function to avoid global variable therefore trouble
    divisor = int(math.sqrt(start)) + 1
    #print number within start and end points if both conditions are true
    if pal(start) and prime(start,divisor):
        print(start)
    #continue recursion as long as starting point less than end point
    if start < end:
        pal_prime (start+1,end)
        
    
def main():
    '''main programe'''
    #get starting point
    start = eval(input ('Enter the starting point N:\n'))
    #get end point
    end = eval(input ('Enter the ending point M:\n'))
    #print welcome message to very famous palindromic numbers
    print ('The palindromic primes are:')
    #call palindrmomic prime function
    pal_prime (start, end)
    
if __name__=="__main__":
    main()