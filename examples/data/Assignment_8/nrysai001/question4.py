# qeustion 4.
# saiheal narayan
# 10 may 2014

import math
import sys
sys.setrecursionlimit(90000000)


def numbers():#inputs
    begin=eval(input('Enter the starting point N:\n'))
    end=eval(input('Enter the ending point M:\n'))
    return begin,end

def checks(number):
    # if palindrome

    if (len(number) <= 1):
        return True
    elif number[0] == number[-1]: 
        return checks(number[1:-1]) 
    else:
        return False 
    
    
def rep(begin, end):
    if (begin == end+1): 
            return
    else:
            if checks( str(begin) ) == True: 
                if Prime(begin,2) == True: 
                    print(begin)              
            return rep(begin+1,end) 
    
def Prime(number, divisor): 
    if number==0 or number==1:
        return False      
    elif divisor>math.sqrt(number):
        return True     
    elif number%divisor==0:
        return False 
    else: 
        return Prime(number, divisor+1) 
    	
    

def main():
    begin,end=numbers() 
    print('The palindromic primes are:') 
    rep(begin,end)    
main()