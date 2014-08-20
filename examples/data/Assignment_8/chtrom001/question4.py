# qeustion4.py 
#program check if number is a palindromic prime
# romelon chetty
# 8 may 2014

import math
import sys
sys.setrecursionlimit (30000)



def get_number():
    # This function is used to get the input from the user
    # the two numbers are then returned for use in the next
    # functions.
    start=eval(input('Enter the starting point N:\n'))
    end=eval(input('Enter the ending point M:\n'))
    return start,end

def Pal(num):
    # This function is used to check the numbers for palindromic
    # validity.
    if (len(num) <= 1): # only one character are both palindromes
        return True
    elif num[0] == num[-1]: #check first letter against last letter
        return Pal(num[1:-1]) # if true runs a smaller part of string in function
    else:
        return False # if first not equal last ,condition is already not met
    
    
def repeat(start, end): #runs through the range inputed and pulls out palindromic primes
    if (start == end+1): #returns nthing if theres not range
        return
    else:
        if Pal( str(start) ) == True: # so if a number is firstly a palindrome then if going to check if it prime
            if checkPrime(start,2) == True: # if the number is also prime 
                print(start)                # then it will print the number
        return repeat(start+1,end) # otherwise the next number is checked
    
def checkPrime(num, divisor): 
    # it going to check a number'num'  is its divisible by numbers from 2 to "num"
    if num==0 or num==1:
        return False      # zero and one are not primes mathematical
    elif divisor>math.sqrt(num):
        return True    # says a divisor  is greater than the square of 'num', it is prime 
    elif num%divisor==0:
        return False #if divisor is a factor of number return false
    else: 
        return checkPrime(num, divisor+1) #checks next divisor
    	
    

def main():
    start,end=get_number() 
    print('The palindromic primes are:') # print the palindromic primes
    repeat(start,end)    
    
main()