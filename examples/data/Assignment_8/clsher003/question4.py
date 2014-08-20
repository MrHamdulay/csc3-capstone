"""calculate palindromic primes in a range
herman claassens
9 may 2014"""


import math
import sys
sys.setrecursionlimit (30000)
    
def palindrome(number):
    number=str(number)  # turn number into string   
    if len(number)<2:   # if string is one character return true
        return True
    if number[-1]!=number[0]:      
        return False
    return palindrome(number[1:-1]) # return the remaining string
    
    
def prime(number,first_number): # devide starting at 2
        if number==1:
                return False     # one is not prime
        if number%first_number==0:
                return False       # checks for non prime
        elif first_number>=int(math.sqrt(number)):
                return True        # stop recursion when the next denominator is equal to the swuare of the nominator
        if number%first_number!=0:   # as long as the number is not devisible keep deviding it
            return prime(number,first_number+1)
        


def prime_palin(num1,num2):
        if num1==1 :
            print(2)
        if num1==num2:   # base case, once all values have been recursed
            return      
        if palindrome(num1)==True and prime(num1,first_number)==True:
            print(num1)     # if the number is a palindromic and a prime, print the number
            return prime_palin((num1+1),num2) # recurse the next number
        else:
            return prime_palin((num1+1),num2) # else just continue to the next number

first_number=2
num1=eval(input("Enter the starting point N:\n"))
num2=eval(input("Enter the ending point M:\n"))
print('The palindromic primes are:')
prime_palin(num1,num2+1)
                
        
            
    
    
        
    